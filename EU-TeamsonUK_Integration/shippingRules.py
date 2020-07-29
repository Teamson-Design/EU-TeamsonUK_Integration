

def getSAPShippingMethod(config, order):
    shippingMethod = {}
    RemotePostcodeList = config['RemotePostcodeList']
    HeavySkuList = config['HeavySkuList']
    OversizedSkuList = config['OversizedSkuList']
    EUSkuList = config['EUSkuList']

    postcodeArea = order['shipping']['postcode'][:2]
    HeavySku = False
    OversizedSku = False
    for line in order['line_items']:
        if line['sku'] in HeavySkuList:
            HeavySku = True
        if line['sku'] in OversizedSkuList:
            OversizedSku = True
        if line['sku'] in EUSkuList:
            EUSku = True

    if postcodeArea in RemotePostcodeList:
        if HeavySku:
            '''UK Pallet - Dachser on site'''
            shippingMethod['shippingCode'] = 36
            shippingMethod['warehouse'] = 'BRAYS'
        if OversizedSku:
            '''Tuffnell Three Day'''
            shippingMethod['shippingCode'] = 14
            shippingMethod['warehouse'] = 'BRAYS'
        else:
            '''DPD Two Day'''
            shippingMethod['shippingCode'] = 4
            shippingMethod['warehouse'] = 'BRAYS'
    elif order['shipping']['country'] == 'GB':
         if HeavySku:
             '''UK Pallet - Dachser on site'''
             shippingMethod['shippingCode'] = 36
             shippingMethod['warehouse'] = 'BRAYS'
         if OversizedSku:
             '''Tuffnell Next Day'''
             shippingMethod['shippingCode'] = 13
             shippingMethod['warehouse'] = 'BRAYS'
         else:
             '''DPD One Day'''
             shippingMethod['shippingCode'] = 3
             shippingMethod['warehouse'] = 'BRAYS'
    # 13/07/20 - changes for no stock in FSS - No orders to FSS
    # else:
    #      if EUSku:
    #          '''UPS Standard Single'''
    #          shippingMethod['shippingCode'] = 21
    #          shippingMethod['warehouse'] = 'FSS'
    #      else:
    #          '''DPD Classic Home'''
    #          shippingMethod['shippingCode'] = 19
    #          shippingMethod['warehouse'] = 'FSS'
    else:
         if EUSku:
             '''cannot be shipped'''
             shippingMethod = {}
         else:
             '''UK DPD International Classic (Road)'''
             shippingMethod['shippingCode'] = 15
             shippingMethod['warehouse'] = 'BRAYS'

    return shippingMethod