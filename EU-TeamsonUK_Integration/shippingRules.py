

def getSAPShippingMethod(config, order):
    shippingMethod = {}
    RemotePostcodeList = config['RemotePostcodeList']
    XDPSkuList = config['XDPSkuList']
    TuffnellsSkuList = config['TuffnellsSkuList']
    EUSkuList = config['EUSkuList']

    postcodeArea = order['shipping']['postcode'][:2]
    XDPSku = False
    TuffnellsSku = False
    for line in order['line_items']:
        if line['sku'] in XDPSkuList:
            XDPSku = True
        if line['sku'] in TuffnellsSkuList:
            TuffnellsSku = True
        if line['sku'] in EUSkuList:
            EUSku = True

    if postcodeArea in RemotePostcodeList:
        if XDPSku:
            '''XDP 2-3 days'''
            shippingMethod['shippingCode'] = 30
            shippingMethod['warehouse'] = 'BRAYS'
        if TuffnellsSku:
            '''Tuffnell Three Day'''
            shippingMethod['shippingCode'] = 14
            shippingMethod['warehouse'] = 'BRAYS'
        else:
            '''DPD Two Day'''
            shippingMethod['shippingCode'] = 4
            shippingMethod['warehouse'] = 'BRAYS'
    elif order['shipping']['country'] == 'GB':
         if XDPSku:
             '''XDP Next Day'''
             shippingMethod['shippingCode'] = 29
             shippingMethod['warehouse'] = 'BRAYS'
         if TuffnellsSku:
             '''Tuffnell Next Day'''
             shippingMethod['shippingCode'] = 13
             shippingMethod['warehouse'] = 'BRAYS'
         else:
             '''DPD One Day'''
             shippingMethod['shippingCode'] = 3
             shippingMethod['warehouse'] = 'BRAYS'
    else:
         if EUSku:
             '''UPS Standard Single'''
             shippingMethod['shippingCode'] = 21
             shippingMethod['warehouse'] = 'FSS'
         else:
             '''DPD Classic Home'''
             shippingMethod['shippingCode'] = 19
             shippingMethod['warehouse'] = 'FSS'

    return shippingMethod