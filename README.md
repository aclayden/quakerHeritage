# quakerHeritage
Project to support the collation of PDF data on the Quaker Meeting House Heritage Project into a database

[![Python 3.10](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/downloads/release/python-3100/)
![status](https://img.shields.io/badge/status-in%20development-orange)

## Required libraries

* bs4
* csv
* io
* numpy
* pandas
* pdfplumber
* re
* requests
* urllib3

## Dependencies

This project has been specifically coded for the Quaker Meeting House Heritage Project, both in hard-coded variables, and hard-coded parameters for extracting text. It is a tool to suit a very specific use-case and may not work if used otherwise. The project further depends on the files required being listed online at the URLs provided. If Britain Yearly Meeting take down the website and associated pdfs, back-ups are available on the Internet Archive's Wayback Machine. The code can also be adapted to work with locally downloaded pdfs. go to Appendix (Local Files) to note the required changes. 

## Components

**1. getWebData.py**

The getWebData component has two methods that use BeautifulSoup and requests to query the Britain Yearly Meeting website for the pdfs held relating to the Quaker Meeting House Heritage Project. These are held on a single subdomain—heritage.quaker.org.uk—and listed as a series of links. The component makes use of pdfplumber to extract the text from the pdf in the chosen section ("Core Data"), after which the method hygienes the data into a dictionary. 

This component is scalable based on inputs, and only returns a single dictionary for a single url.
    
**2. cleanseData.py**

The cleanseData component has several data manipulation methods to transform the dictionaries produced by the getWebData methods into a single Pandas Dataframe. As the dictionary keys from the pdfs are inconsistent, the first dictionary is used as the master and its keys form the column headings. The remaining dictionaries have their values stripped off into lists, and are then inserted into the Dataframe. To meet user requirements, further methods transform certain raw string data to form date or numeric fields that can be more easily worked upon.

This component does not require scaling, as the variable passed to the createDataFrame method can be of any length. 
