# from urllib.parse import urlencode
import grpc
# import logging
# from logging import LoggerAdapter
# #import logstash
# import requests
# import sys
# #import toml
# import urllib.request
# import json
# import base64

from woocommerce import API

'''imports for usability server'''
from uk.data.ar.sales_order import BasicSalesOrder_pb2
from uk.data.ar.delivery_order import BasicDeliveryOrder_pb2
from uk.networking.requests.ar.delivery_order import GetDeliveryTrackingRequest_pb2, GetBasicDeliveryOrdersRequest_pb2
from uk.networking.requests.ar.sales_order import InsertBasicSalesOrderRequest_pb2
from uk.networking.requests.item.stock import GetStockInfoRequest_pb2

from datetime import datetime

''' Read from Teamson: Orders, Stock, Tracking'''
def readFromTeamson (callType, orderId, logger):
    consumerKey = 'ck_ec85a078781e4d60bb175c61c24fac0d8a224dd1'
    consumerSecret = 'cs_05d24b657774ad736cd69058d003a3f1d3ea4c84'
    optionMap = {"orders": {"route": "","version": "wc/v3/orders", 'params': "&per_page=100&status=processing", "pagination": True},
    "stocks": {"route": "","version":  "wc/v3/products", 'params': "&per_page=100", "pagination": False},
    "tracking": { "version":  "wc/v3", 'params': "", "pagination": False}}
    optionMap['tracking']['route'] = "orders/" + orderId + "/shipment-trackings"
    options = optionMap[callType]

    wcapi = API(
        url="https://teamson.co.uk",
        consumer_key=consumerKey,
        consumer_secret=consumerSecret,
        wp_api=True,
        version=options['version']
    )
    page = 1
    data = []
    pageData = []
    try:
        pageData = wcapi.get(options['route'] + "?page=" + str(page) + options['params']).json()
    except:
        logger.error("Failed to read data from Teamson...")
    while pageData != []:
        page += 1
        data[len(data):] += pageData
        if options['pagination']:
            try:
                pageData = wcapi.get(route + "?page=" + str(page) + params).json()
            except:
                logger.error("Failed to read next page from Teamson...")
                pageData = []
        else:
            pageData = []
    return data

def readSAPStock(stubGetStockInfoService, logger):

    stockInfoRequest = GetStockInfoRequest_pb2.GetStockInfoRequest(item_scope='ALL_ITEMS',
                                                                   bom_handler='SPECIFIC_WAREHOUSE',
                                                                   specified_warehouses={'BRAYS', 'FSS'})
    try:
        stockInfoResponses = stubGetStockInfoService.GetStockInfo(stockInfoRequest)
    except grpc.RpcError:
        logger.error("Failed to read Stock values from SAP..." )
    else:
        logger.debug("Stock values successfully read from SAP... " )

    '''Calculate Buffer adjustment 10 over the weekend (midday friday(4) to midday Monday(0)) and  5 during the week'''
    weekday = datetime.now().weekday()
    hour = datetime.now().timetuple()[3]
    stockBuffer = 5 # weekday value
    if (weekday >= 4 and hour >= 12) or (weekday == 0 and hour <= 12):
        stockBuffer = 10 # Weekend value

    '''loop through all stock items in SAP'''
    SAPStockDict = {}
    stockInfos = []
    for SAP_Item in stockInfoResponses:
        stockInfos.append(SAP_Item)
        if SAP_Item.is_active and not SAP_Item.is_component:
            itemTotal = 0
            whsDict = {}
            for warehouseStock in SAP_Item.warehouse_stock:
                SAP_whscde = warehouseStock.warehouse.upper()
                if SAP_whscde != '':
                    availableStock = warehouseStock.on_hand - warehouseStock.commited
                    whsDict[SAP_whscde] = availableStock
                    whsDict[SAP_whscde + 'Adj'] = 0
                    if availableStock > stockBuffer:
                        whsDict[SAP_whscde+'Adj'] = availableStock - stockBuffer
                    itemTotal += availableStock
            ''' Add total and adjusted total to dictionary '''
            whsDict['total'] = itemTotal
            itemTotalAdj = 0
            if (itemTotal - stockBuffer) > 0:
                itemTotalAdj = itemTotal - stockBuffer
            whsDict['totalAdj'] = itemTotalAdj
            SAPStockDict[SAP_Item.item_code] = whsDict
    '''get lowest child stocks for Sets (Bundles)'''
    for SAP_Item in stockInfos:
        if SAP_Item.is_active and SAP_Item.is_component:
            itemTotal = 0
            lowestItem = ''
            whsDict = {}
            for childItem in SAP_Item.child_items:
                if childItem.is_active:
                    childItemAvailable = childItem.warehouse_stock[1].on_hand - childItem.warehouse_stock[1].commited
                if childItemAvailable > 0 and itemTotal == 0 and lowestItem == '':
                    itemTotal = childItemAvailable
                    lowestItem = childItem.item_code
                elif childItemAvailable > 0 and childItemAvailable < itemTotal:
                    itemTotal = childItemAvailable
                    lowestItem = childItem.item_code
                elif childItemAvailable == 0:
                    itemTotal = childItemAvailable
                    lowestItem = childItem.item_code
            SAPStockDict[SAP_Item.item_code] = SAPStockDict[lowestItem]
    return SAPStockDict

def readSAPTracking (stubGetDeliveryOrders, stubGetTrackingNumber):
    DNRequest = GetBasicDeliveryOrdersRequest_pb2.GetBasicDeliveryOrdersRequest()
    DNRequest.filter_uploaded_lines=False
    DNRequest.specified_statuses.extend([0])  # 0-'OPEN' and/or 1-'CLOSED'
    DNRequest.specified_warehouses.extend(['FSS', 'Brays'])
    DNRequest.specified_order_types.extend([0])  # 'ITEM'
    #DNRequest.specified_customer_orders.update(customerOrders)  # 'cust ref'
    try:
        DNResponse = stubGetDeliveryOrders.GetBasicDeliveryOrders(DNRequest)
    except grpc.RpcError as err:
        logger.error('unable to read delivery notes for tracking from SAP, order: ' + customerOrderNumber)

    DNS = []
    for DN in DNResponse:
        if DN.business_partner == 'DIRECT16':
            TrackingRequest = GetDeliveryTrackingRequest_pb2.GetDeliveryTrackingByOrderNumberRequest \
                (order_number=DN.order_number)
            TrackingResponse = stubGetTrackingNumber.GetDeliveryTrackingByOrderNumber(TrackingRequest)
            trackingNum = TrackingResponse.tracking_number
            if trackingNum != "":
               DNS += [{'DN':DN,'trackingNum':trackingNum}]
    return DNS

def writeSAPOrder (stubInsertSalesOrder,SAPOrder,logger):
    logger.debug('insert order for order:  ' + SAPOrder.order_number)
    try:
        insertRequest = InsertBasicSalesOrderRequest_pb2.InsertBasicSalesOrderRequest(order_to_insert=SAPOrder)
        stubInsertSalesOrder.InsertBasicSalesOrder(insertRequest)
    except grpc.RpcError:
        logger.error("insert order request failed, order: " + order['SiteOrderID'])
    else:
        logger.info("INFO - Order successfully imported: " + SAPOrder.customer_order_number)

def writeToTeamson(callType, id, data, logger):

    consumerKey = 'ck_ec85a078781e4d60bb175c61c24fac0d8a224dd1'
    consumerSecret = 'cs_05d24b657774ad736cd69058d003a3f1d3ea4c84'
    optionMap = {"stocks": {"version": "wc/v3"}, "tracking": {"version": "wc/v3"}}
    optionMap['stocks']['route'] = "products/" + str(id)
    optionMap['tracking']['route'] = "orders/" + str(id) + "/shipment-trackings"
    options = optionMap[callType]
    wcapi = API(
        url="https://teamson.co.uk",
        consumer_key=consumerKey,
        consumer_secret=consumerSecret,
        wp_api=True,
        version=options["version"]
    )
    try:
        ret = wcapi.post(options["route"], data).json()
    except:
        logger.error("ERROR - Updating Tracking in Teamson: order: " + str(id) )
    else:
        logger.info('SUCCESS - Tracking Imported: order: ' + str(id))
    return ret