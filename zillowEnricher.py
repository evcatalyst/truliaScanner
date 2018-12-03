import zillow
from turicreate import SFrame


## Get your own Zillow API key (zwsid) here 
## https://www.zillow.com/howto/api/APIOverview.htm


zwsid = <REDACTED ADD YOUR OWN KEY>


key = zwsid
api = zillow.ValuationApi()

def getSearchResults(key,row):
    try:
        address = row['ADDRESS'].strip()
        zipCode = row['ZIP CODE']
        data = api.GetDeepSearchResults(key,address,zipCode)
        return data.get_dict()
    except:
        pass

sf = SFrame.read_csv('trulia11566.csv', verbose=False)
sf['zillowData'] = sf.apply(lambda row: getSearchResults(key,row))

sf = sf.unpack('zillowData').unpack('zillowData.zestimate')


sf['ADDRESS',
   'LOCALITY',
   'STATE',
   'ZIP CODE',
   'COUNTY',
   'STREET',
   'TYPE',
   'PRICE',
   'zillowData.zestimate.amount',
   'zillowData.zestimate.valuation_range_high',
   'zillowData.zestimate.valuation_range_low',
   'DAYS POSTED',
   'BEDS',
   'BATHS',
   'BUILD DATE',
   'LOT SIZE',
   'SQFT',
   'FEES',
   'VIEW COUNT',
   'DESCRIPTION'].export_csv('truliaZillow11566.csv')


