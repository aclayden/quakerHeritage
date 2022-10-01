# Quaker Heritage Project Documentation

This website contains the project documentation for the `quakerheritage` project, which seeks to use the publicly published information on several hundred pdfs and merge itinto a useful and workable database for the purposes of research or administration. The original documentation can be found on the [Heritage section of the Britain Yearly Meeting website](https://heritage.quaker.org.uk). 

The aim of this project is to assist the Society of Friends with making the most of the hard work invested in the project by allowing the core data to be worked upon and kept up to date.

## Summary

The project at present isn't robust enough to require multiple pages, nor lengthy explanations of configurable functions. The design principles of the project were to build a tailored set of code modules to solve a very specific problem. As a result, the modules and functions in this project could be adapted for other use cases, but perform best when used without amendment to create the csv output from the Heritage Project data. 

## How-To

In order to run the code, simply open your terminal and run the following:

    python -m quakerheritage.build

## build
Unifies the functional modules and runs the main code to create a formatted Pandas DataFrame from pdfs held by Britain Yearly Meeting.

This module runs automatically when opened, in concert with the other modules in this package. 

This module contains the following functions:

- `getOnlineData(url)` - Collects pdfs from webpage, extracts text to dictionary, creates DataFrame from all dicitonaries and hygienes data.

#### getOnlineData(url: str)
Collect online data and merge it into a Pandas DataFrame
    
    Args:
        url (string): A fixed URL for the Quaker Meeting House Heritage Project's pdf storage.
        
    Returns:
        df (Pandas DataFrame): A transformed and hygeined DataFrame.
        
## cleanseData
Runs Pandas functionality to merge text data into workable DataFrame and creates consistent data quality.

This module allows the user to take the raw data from the Quaker Heritage Project's pdfs and enhances usefulness of data points and types.

This module contains the following functions:

- `createDataframe(url)` - Takes a list of dictionaries with varied values and keys and unifies them into a single Pandas DataFrame.
- `hygieneDataFrame(df)` - Takes the varied data in the DataFrame and applies a regular schema to it for data quality purposes.

#### createDataFrame(dictList: list)
Concatenates dictionary values and transforms them into a Pandas DataFrame.

    Args:
        dictList (array): A list object of dictionaries created from pdfs.

    Return:
        df (Pandas DataFrame): A raw and unhygiened Pandas DataFrame.

#### hygieneDataFrame(df: pd.DataFrame)
Data quality function that iterates through selected columns within the DataFrame and corrects variant values.

    Example:
        'Date of Visit': 
            Old Value: 5th July 2015
            Hygiened Value: 2015-07-05
        'Date':
            Old Value: c1864-70, 1965; 2005
            Hygiened Value: 1864

    Args:
        df (Pandas DataFrame): A raw and unhygiened DataFrame.

    Return:
        df (Pandas DataFrame): The same DataFrame with all formatting applied for data quality.
        
## getWebData
Main web function that collects url data and extracts text from each pdf examined.

This module allows the user to extract core data from formatted pdfs on the Britain Yearly Meeting website.

This module contains the following functions:

- `getUrls(url)` - Filters the Quaker Heritage Project's website for the url links to pdfs.
- `pdfDataExtract(url)` - Extracts core data text from a single pdf passed in as a url link.

#### getUrls(url: str) -> list:
Short function to isolate links from the chosen web page. As the webpage is pre-selected, they are all known to be pdf files.

    Args:
        url (string): the pre-selected web address.

    Return:
        pdfList(array): a Python list containing all the links extracted from the page. 
        
#### pdfDataExtract(url: str) -> dict:
Extracts text data from pdfs and passes it into a dictionary

    Args:
        url (string): a single url which must be a pdf file storage location.

    Return:
        itemDict (array): Python dictionary containing keys and values extracted from text.
