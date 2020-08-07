import grpc
import logging
import toml
from datetime import datetime

from integrationTools import readFromTeamson, readSAPStock, readSAPTracking, writeSAPOrder, writeToTeamson
from orderMap import orderMap

from uk.data.ar.sales_order import BasicSalesOrder_pb2
from uk.networking.requests.ar.sales_order import GetSalesOrderStatusRequest_pb2
from uk.networking.services.ar.delivery_order import GetDeliveryTrackingService_pb2_grpc, \
    GetBasicDeliveryOrdersService_pb2_grpc
from uk.networking.services.ar.sales_order import GetBasicSalesOrderInfoService_pb2_grpc, \
    InsertBasicSalesOrderService_pb2_grpc
from uk.networking.services.item.stock import GetStockInfoService_pb2_grpc

'''------------import the new orders into SAP---------------'''
def importOrders(config, stubGetBasicSalesOrderInfo, stubInsertSalesOrder, businessPartner, logger):
    '''loop through the sites importing orders'''
    orderSitesList = config['orderSitesList']
    for site in orderSitesList:
        orders = readFromTeamson(config, site, 'orders', '', logger)
        for order in orders:
            SAPOrder = orderMap(config, order, businessPartner, logger)
            if SAPOrder == '':
                logger.error("Failed to Map order for SAP: " + '#' + str(order['id']))
            else:
                businessPartner = SAPOrder.business_partner
                customerOrderNumber = SAPOrder.customer_order_number
                request = GetSalesOrderStatusRequest_pb2.GetSalesOrderStatusByCustomerInfoRequest(
                        business_partner=businessPartner, customer_order_number=customerOrderNumber)
                try:
                    response = stubGetBasicSalesOrderInfo.GetSalesOrderStatusByCustomerInfo(request)
                except grpc.RpcError:
                    logger.error("Failed to read order status from SAP...")
                else:
                    logger.debug("order status successfully read from SAP... ")
                    if (response.order_status == 0) & (len(order) > 0):
                        '''create the order(s)'''
                        writeSAPOrder (stubInsertSalesOrder, SAPOrder, logger)
                    elif (response.order_status != 0) & (len(order) > 0):
                        logger.error("Order already exist or is cancelled: " + customerOrderNumber)

    logger.info("Inserted all orders")

'''-----------Update stock quantities in Teamson------------'''
def updateStockQty(config, stubGetStockInfoService, logger):
    SAPStockDict = readSAPStock(config, stubGetStockInfoService, logger)
    '''loop through the sites importing orders'''
    stockSitesList = config['stockSitesList']
    for site in stockSitesList:
        TeamsonStocks = readFromTeamson(config, site, 'stocks', '', logger)
        for stock in TeamsonStocks:
            doNotUpdate = False
            useBrays = False
            useFSS = False
            for tag in stock['tags']:
                if tag['slug'] == 'no-stock-revise':
                     doNotUpdate = True
                elif tag['slug'] == 'oversized-uk':
                    useBrays = True
                elif tag['slug'] == 'oversized-eu':
                    useFSS = True
            '''---- 14/07/20 SD All stock from Brays only ----'''
            if not doNotUpdate:
                useBrays = True
            if stock['sku'] in SAPStockDict and not doNotUpdate:
                if useBrays:
                    if stock['stock_quantity'] != SAPStockDict[stock['sku']]['BRAYSAdj']:
                        logger.debug ('SKU = ' + stock['sku'] + ', Teamson.co.uk = ' + str(stock['stock_quantity']) +
                               ', SAP(Brays) = ' + str(SAPStockDict[stock['sku']]['BRAYS']) + ', SAP(Adjusted-Brays) = ' +
                               str(SAPStockDict[stock['sku']]['BRAYSAdj']) + ', tags: ' + str(stock['tags']))
                        data = {"stock_quantity": SAPStockDict[stock['sku']]['BRAYSAdj']}
                        ret = writeToTeamson (config, site, 'stocks', stock['id'],data, logger)
                else:
                    if stock['stock_quantity'] != SAPStockDict[stock['sku']]['totalAdj']:
                        logger.debug ('SKU = ' + stock['sku'] + ', Teamson.co.uk = ' + str(stock['stock_quantity']) +
                               ', SAP(Brays) = ' + str(SAPStockDict[stock['sku']]['BRAYS']) + ', SAP(Adjusted-Total) = ' +
                               str(SAPStockDict[stock['sku']]['TotalAdj']) + ', tags: ' + str(stock['tags']))
                        data = {"stock_quantity": SAPStockDict[stock['sku']]['totalAdj']}
                        ret = writeToTeamson (config, site, 'stocks', stock['id'], data, logger)

            elif doNotUpdate:
                 logger.debug("sku id tagged as 'do not update':"  + stock['sku'])
            else:
                 logger.error("sku does not exist in SAP: " + stock['sku'])

    logger.info("Updated stocks")

'''---------------Update tracking in Teamson----------------'''
def importTracking(config, stubGetTrackingNumber, stubGetTrackingService, stubGetDeliveryOrders):
    DNS = readSAPTracking (stubGetDeliveryOrders, stubGetTrackingNumber)
    orderSitesList = config['orderSitesList']
    for site in orderSitesList:
        for trackingDict in DNS:
            DN = trackingDict['DN']
            orderId = DN.customer_order_number[1:len(DN.customer_order_number)] # strip # from orderID
            trackingNum = trackingDict['trackingNum']
            if len(DN.shipping_method) < 21:
                provider = DN.shipping_method[3: 6]
            else:
                provider = 'Tuffnells'
            dateTime = datetime.now().strftime('%m/%d/%Y')
            trackingInfos = readFromTeamson(config, site, 'tracking', orderId,  logger)
            if trackingInfos == []:
                if provider == 'Tuffnells' and len(trackingNum) < 10:
                    logger.debug("Tuffnells Temporary Tracking Number skipped...")
                else:
                    data = {
                    'tracking_number': trackingNum,
                    'tracking_provider': provider
                    }

                    logger.debug(str(data))
                    ret = writeToTeamson(config, site, 'tracking', orderId, data, logger)
                    data = {
                    'status': 'completed'
                    }
                    logger.debug(str(data))
                    ret = writeToTeamson(config, site, 'orders', orderId, data, logger)
    logger.info("imported Tracking")

'''------------------------------------------------------------------------------------------------------------------'''
'''Main program starts here'''
toml_file = "C:/eCommerce Connections/EMEA/UK/Teamson UK/integration_config.toml"
config = toml.load(toml_file)

businessPartner = config['businessPartner']
#channelMap = config['ChannelMap']
shippingMap = config['ShippingMap']
revShipMap = config['RevShipMap']

'''------------set up logging file----------'''
logging_file = config['Teamson_logging_file']

'''------------account server info---down--------'''
usabilityHost = config['usabilityHost']
usabilityPort = config['usabilityPort']
Channel = usabilityHost + usabilityPort

'''------------account server info-----up------'''

'''logging file create '''
logging.basicConfig(filename=logging_file, filemode="w",
                    format='%(asctime)s  %(levelname)s - %(message)s',
                    datefmt='%d/%m/%Y %H:%M', level=logging.INFO)
logger = logging.getLogger(__name__)
# adapter = LoggerAdapter(logger, {"sub-level":"ORDER_IMPORT_SUCCESS"})

'''----------------create client STUB-----------------'''
try:
    logger.debug(" Building server channels...")
    channel = grpc.insecure_channel(Channel)
    stubGetStockInfoService = GetStockInfoService_pb2_grpc.GetStockInfoServiceStub(channel)
    stubGetBasicSalesOrderInfo = GetBasicSalesOrderInfoService_pb2_grpc.GetBasicSalesOrderInfoServiceStub(channel)
    stubInsertSalesOrder = InsertBasicSalesOrderService_pb2_grpc.InsertBasicSalesOrderServiceStub(channel)
    stubGetDeliveryOrders = GetBasicDeliveryOrdersService_pb2_grpc.GetBasicDeliveryOrdersServiceStub(channel)
    stubGetTrackingNumber = GetDeliveryTrackingService_pb2_grpc.GetDeliveryTrackingServiceStub(channel)
    stubGetTrackingService = GetDeliveryTrackingService_pb2_grpc.GetDeliveryTrackingServiceStub(channel)

except grpc.RpcError:
    logger.error("channels... failed: ")
    sys.exit(0)
'''------------import the new orders into SAP---------------'''
importOrders(config, stubGetBasicSalesOrderInfo, stubInsertSalesOrder, businessPartner, logger)
'''-----------Update stock quantities in Teamson------------'''
updateStockQty(config, stubGetStockInfoService, logger)
# '''---------------Update tracking in Teamson----------------'''
# importTracking(config, stubGetTrackingNumber, stubGetTrackingService, stubGetDeliveryOrders)

