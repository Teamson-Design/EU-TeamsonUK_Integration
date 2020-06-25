from uk.data.ar.sales_order import BasicSalesOrder_pb2
from shippingRules import getSAPShippingMethod

def orderMap (config, order, businessPartner, logger):
    shippingMethod = getSAPShippingMethod(config, order)

    BasicOrderInfo = BasicSalesOrder_pb2.BasicSalesOrder()
    BasicOrderInfo.business_partner = businessPartner
    BasicOrderInfo.order_total = float(order['total'])
    BasicOrderInfo.order_number = order['number']
    BasicOrderInfo.customer_order_number = '#' + str(order['id'])
    BasicOrderInfo.shipping_method_code = shippingMethod['shippingCode']
    BasicOrderInfo.ship_street = order['shipping']['first_name'] + ' ' + order['shipping']['last_name']
    BasicOrderInfo.ship_street_num = order['shipping']['address_1']
    '''SD 26/05/20, Requested change row[12] (shipping_Address 2) seems to usually contain city and so should 
    be used as such instead of Block. May eventually need some logic here to determine city/block'''
    #BasicOrderInfo.ship_block = row[12]
    #BasicOrderInfo.ship_city = row[13]
    BasicOrderInfo.ship_city = order['shipping']['city']
    BasicOrderInfo.ship_county = order['shipping']['state']
    BasicOrderInfo.ship_zip = order['shipping']['postcode']
    BasicOrderInfo.ship_country = order['shipping']['country']
    BasicOrderInfo.customer_phone = order['billing']['phone']
    BasicOrderInfo.customer_email = order['billing']['email']

    for line in order['line_items']:
        orderLine = BasicOrderInfo.order_lines.add()
        orderLine.item_code = line['sku']
        orderLine.quantity = line['quantity']
        orderLine.price_after_vat = float(line['total'])
        orderLine.warehouse = shippingMethod['warehouse']

    return BasicOrderInfo
