Scanning script to pull data from trulia for a given County and ZipCode

Credit given to tkART/TruliaScrape for the baseline version (https://github.com/tkART/TruliaScrape)

##TODO:
* Clean up code, address issues
* Create a dictionary of relevant fields in a configuration file, and establish an iterator for those fields
* ~Add module to reconcile prices with those from Zillow using the Zillow API (Search on exact address)~
* Import property taxes and school district information
* Output to excel pivot table format based on to be identified criteria, template pivot table and update data.
* Establish multi-zip dictionary matching
* Add email functionality to push the excel report
* Parallelize requests using multiprocessing to speed up from ~10 min on ~120.
* Deployment update to allow for AWS Lambda scheduling
* Add cleaned requirements.txt for user deployment
* Port to use puppeteer and node.js


##Modules
###scanner.py

Module does not require an API key. Pretends to be a user/set of users, scrapes the location index. Filters for the identified locations and sub locations. Then scans all of the properties in that location, extracts selected data and writes the results to a csv file.


###zillowEnricher.py

Module requires the [Zillow API key](https://www.zillow.com/howto/api/APIOverview.htm). Loads the CSV result file from scanner.py and runs a function that queries the Zillow API using the [python-zillow](https://github.com/seme0021/python-zillow) module on the Address and Zip Code of each result. Loads the data into a dictionary, and then unpacks the dictionary into columns, unpacks the zestimate data into columns, then provides the result into a csv file export that contains the data from Zillow with the Zestimate information for each of the properties. 

