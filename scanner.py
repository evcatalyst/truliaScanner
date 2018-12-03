import time
import random
import re
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

countyName = 'Nassau'
zipCode = '11566'
outFile = 'trulia'+str(zipCode)+'.csv'


def getSoup(new_url):
    url = ("https://www.trulia.com" + new_url)
    req = Request(url, headers={'User-Agent': str(uAgents[random.randint(0,3)])})
    web_byte = urlopen(req).read()
    webpage = web_byte.decode('utf-8')
    return BeautifulSoup(webpage, "html.parser")

def scrape(property, street, county, zip, file):

    type = ""
    address = ""
    locality = ""
    region = "NY-Merrick"
    price = ""
    beds = ""
    baths = ""
    built = ""
    days = ""
    lot = ""
    sqft = ""
    views = ""
    fees = ""

    if hasattr(property.find("div", {"data-role":"address"}), 'text'):
        address = property.find("div", {"data-role":"address"}).text.replace("\n", "")
        
## Removed the below property - had inconsistent results
        
    #if hasattr(property.find("div",{"id":"subNavContent"}).find("a", {"onclick":"trulia.analytics.saveInteractedWith('top bar:breadcrumb city link')"}), 'text'):
    #    locality = property.find("div",{"id":"subNavContent"}).find("a", {"onclick":"trulia.analytics.saveInteractedWith('top bar:breadcrumb city link')"}).text

    
    if hasattr(property.find("span", {"data-role":"price"}), 'text'):
        price = property.find("span", {"data-role":"price"}).text.replace(",", "")
        price = price.replace("\n", "")
        price = price.replace(" ", "")

    list = property.find("div",{"data-auto-test-id":"home-details-overview"}).findAll("li", recursive=True)

    for li in list:
        text = li.getText()


#    Use a generator together with any, which short-circuits on the first True:
#    if any(ext in url_string for ext in extensionsToCheck):
#        print(url_string)

        if "Single-Family Home" in text:
            type =  re.sub(r'^\s*','', text)
        elif "Condo" in text:
            type =  re.sub(r'^\s*','', text)
        elif "Townhouse" in text:
            type =  re.sub(r'^\s*','', text)
        elif "Mobile/Manufactured" in text:
            type =  re.sub(r'^\s*','', text)
        elif "Multi-Family" in text:
            type =  re.sub(r'^\s*','', text)
        elif "Lot/Land" in text:
            type =  re.sub(r'^\s*','', text)
        elif "Unknown" in text:
            type =  re.sub(r'^\s*','', text)


        elif "Bed" in text:
            beds = re.sub(r'\s*[A-Za-z]*\s*','', text)
        elif "Bath" in text:
            baths = re.sub(r'\s*[A-Za-z]*\s*','', text)
        elif "Built" in text:
            built = re.sub(r'\s*[A-Za-z]*\s*','', text)
        elif "days" in text:
            days = re.sub(r'\s*[A-Za-z]*\s*','', text)
            days = days.replace(",","")
        elif "lot" in text:
            lot = re.sub(r'\s*[A-Za-z]*\s*','', text)
        elif " sqft" in text:
            sqft = re.sub(r'\s*[A-Za-z]*\s*','', text)
            sqft = sqft.replace(",", "")
        elif "view" in text:
            views = re.sub(r'\s*[A-Za-z]*\s*','', text)
        elif "monthly" in text:
            fees = re.sub(r'\s*[A-Za-z]*\s*','', text)

    description = property.find("p",{"id":"propertyDescription"}).getText().replace("\n","")
    description = description.replace(",", "")
    description = description.replace("\n", "")
    description = re.sub(r'^\s*','', description)

    county = re.sub(r'^\s*','', county)

    print("County:\t\t" + county)
    print("Zip:\t\t" + zip.replace(" ",""))
    print("Street:\t\t" + re.sub(r'\(.*\)','', street))
    print("Address:" + address.replace("\n", ""))
    print("Locality:\t" + locality)
    print("Type:\t\t" + type)
    print("Price:\t\t" + price)
    print("Beds:\t\t" + beds)
    print("Baths:\t\t" + baths)
    print("Built:\t\t" + built)
    print("Listed:\t\t" + days)
    print("Lot:\t\t" + lot)
    print("Sqft:\t\t" + sqft)
    print("Views:\t\t" + views)
    print("Fees:\t\t" + fees)
    print("\n" + description + "\n")

    file.write(address + "," + locality + "," + region + "," + zip + ","  + county + "," + street + "," + type + "," + price + "," + beds + "," + baths + "," + built + "," + lot + "," + sqft + "," + fees + "," + days + "," + views + "," + description + "\n")
#   f.write("ADDRESS" + "," + "LOCALITY" + "," + "STATE" + "," + "ZIP CODE" + "," + "COUNTY" + "," + "STREET" + "," + "TYPE" + "," + "PRICE" + "," + "BEDS" + "," + "BATHS" + "," + "BUILD DATE" + "," + "LOT SIZE" + "," + "SQFT" + ","  + "FEES" + "," + "VIEW COUNT" + ","  + "DAYS POSTED" + "," + "DESCRIPTION" + "\n")



uAgents = ['Mozilla/5.0', 'AppleWebKit/537.36', 'Chrome/68.0.3440.106', 'Safari/537.36']
proxies = ['178.128.101.193', '159.89.238.0', '149.56.140.20', '167.99.0.181', '64.105.51.186', '162.223.89.92']

url='https://www.trulia.com/sitemap/New-York-real-estate/'
req = Request(url, headers={'User-Agent': 'Chrome/68.0.3440.106'})
web_byte = urlopen(req).read()
webpage = web_byte.decode('utf-8')
soup = BeautifulSoup(webpage, "html.parser")

filename = outFile
f = open(filename, "w")
f.write("ADDRESS" + "," + "LOCALITY" + "," + "STATE" + "," + "ZIP CODE" + "," + "COUNTY" + "," + "STREET" + "," + "TYPE" + "," + "PRICE" + "," + "BEDS" + "," + "BATHS" + "," + "BUILD DATE" + "," + "LOT SIZE" + "," + "SQFT" + ","  + "FEES" + "," + "VIEW COUNT" + ","  + "DAYS POSTED" + "," + "DESCRIPTION" + "\n")

homeCount = 0
counties = soup.find("ul",{"class":"all-counties-sitemap-links"}).findAll("a", recursive=True)

for county in counties:
    if countyName in county.text:
        time.sleep(10)
        soup = getSoup(county.get('href'))
        zip_codes = soup.find("ul",{"class":"all-zip-codes-sitemap-links"}).findAll("a", recursive=True)
        county_txt = county.text.replace(" County","")

        for zip in zip_codes:
            if zipCode in zip.text:
                time.sleep(random.randint(2, 4))
                soup = getSoup(zip.get('href'))
                streets = soup.find("ul",{"class":"all-streets-sitemap-links"}).findAll("a", recursive=True)
                zip_txt = zip.text

                for street in streets:
                    time.sleep(random.randint(1, 2))
                    soup = getSoup(street.get('href'))
                    street_txt =  re.sub(r'\s*\(.*\)','', street.text)

                    if  soup.find("ul", {"class":"all-properties-sitemap-links"}) == None:
                        homeCount += 1
                        property = soup
                        print("ELEMENT:  " + str(homeCount))
                        scrape(property, street_txt, county_txt, zip_txt, f)
                    else:
                        properties = soup.find("ul",{"class":"all-properties-sitemap-links"}).findAll("a", recursive=True)
                        for property in properties:
                            homeCount += 1
                            time.sleep(random.randint(2, 3))
                            soup = getSoup(property.get('href'))
                            print("ELEMENT:  " + str(homeCount))
                            scrape(soup, street_txt, county_txt, zip_txt, f)
    else:
        pass
f.close()