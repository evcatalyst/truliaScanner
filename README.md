Scanning script to pull data from trulia for a given County and ZipCode

Credit given to tkART/TruliaScrape for the baseline version (https://github.com/tkART/TruliaScrape)

TODO:
* Clean up code, address issues
* Create a dictionary of relevant fields in a configuration file, and establish an iterator for those fields
* Add module to reconcile prices with those from Zillow using the Zillow API (Search on exact address)
* Import property taxes and school district information
* Output to excel pivot table format based on to be identified criteria, template pivot table and update data.
* Establish multi-zip dictionary matching
* Add email functionality to push the excel report
* Parallelize requests using multiprocessing to speed up from ~10 min on ~120.
* Deployment update to allow for AWS Lambda scheduling
* Add cleaned requirements.txt for user deployment
* Port to use puppeteer and node.js



