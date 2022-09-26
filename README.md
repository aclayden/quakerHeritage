# quakerHeritage
Project to support the collation of PDF data on the Quaker Meeting House Heritage Project into a database 

[![Python 3.10](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/downloads/release/python-3100/)

## Required libraries

* bs4
* csv
* io
* pandas
* pdfplumber
* re
* requests
* urllib3


## Components

**1. getWebData.py**

The getWebData component has two methods that use BeautifulSoup and requests to query the Britain Yearly Meeting website for the pdfs held relating to the Quaker Meeting House Heritage Project. These are held on a single subdomain—heritage.quaker.org.uk—and listed as a series of links. The component makes use of pdfplumber to extract the text from the pdf in the chosen section ("Core Data"), after which the method hygienes the data into a dictionary. 

This component is scalable based on inputs, and only returns a single dictionary for a single url.
    
