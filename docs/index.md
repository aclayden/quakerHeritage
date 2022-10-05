# Quaker Heritage Project Documentation

This website contains the project documentation for the `quakerheritage` project, which seeks to use the publicly published information on several hundred pdfs and merge itinto a useful and workable database for the purposes of research or administration. The original documentation can be found on the [Heritage section of the Britain Yearly Meeting website](https://heritage.quaker.org.uk). 

The aim of this project is to assist the Society of Friends with making the most of the hard work invested in the project by allowing the core data to be worked upon and kept up to date.

## Summary

The project at present isn't robust enough to require multiple pages, nor lengthy explanations of configurable functions. The design principles of the project were to build a tailored set of code modules to solve a very specific problem. As a result, the modules and functions in this project could be adapted for other use cases, but perform best when used without amendment to create the csv output from the Heritage Project data. 

## How-To

In order to run the code, simply open your terminal and run the following:

    python -m quakerheritage.build

You will be prompted to select a location for the csv output to be placed. Once chosen, the code will run quietly in the background until complete, and the csv available at your chosen directory as 'quakerHeritageDB.csv'

## build
Unifies the functional modules and runs the main code to create a formatted Pandas DataFrame from pdfs held by Britain Yearly Meeting.

This module runs automatically when opened, in concert with the other modules in this package. 

This module contains the following functions:

- `get_online_data(url)` - Collects pdfs from webpage, extracts text to dictionary, creates DataFrame from all dicitonaries and hygienes data.
- `main()` - executes automatically to run the entire project

#### get_online_data(url: str)
Collect online data and merge it into a Pandas DataFrame
    
    Args:
        url (string): A fixed URL for the Quaker Meeting House Heritage Project's pdf storage.
        
    Returns:
        df (Pandas DataFrame): A transformed and hygeined DataFrame.
        
## cleanse_data
Runs Pandas functionality to merge text data into workable DataFrame and creates consistent data quality.

This module allows the user to take the raw data from the Quaker Heritage Project's pdfs and enhances usefulness of data points and types.

This module contains the following functions:

- `create_dataframe(url)` - Takes a list of dictionaries with varied values and keys and unifies them into a single Pandas DataFrame.
- `bulk_hygiene_dataframe(df)` - Takes the varied data in the DataFrame and applies a regular schema to it for data quality purposes.

#### create_dataframe(data_list: list)
Concatenates dictionary values and transforms them into a Pandas DataFrame.

    Args:
        data_list (list): A list object of data collated from pdfs.

    Return:
        df (Pandas DataFrame): A raw and unhygiened Pandas DataFrame.

#### bulk_hygiene_dataframe(df: pd.DataFrame)
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

#### save_to_csv(df: pd.DataFrame, file_path: str)
Small function to save CSV with appropriate format.
    
    Args:
        df (Pandas DataFrame): collection of data for Pandas to convert to CSV.
        file_path (string): desired location for file creation.

## get_web_data
Main web function that collects url data and extracts text from each pdf examined.

This module allows the user to extract core data from formatted pdfs on the Britain Yearly Meeting website.

This module contains the following functions:

- `get_urls(url)` - Filters the Quaker Heritage Project's website for the url links to pdfs.
- `pdf_data_extract(url)` - Extracts core data text from a single pdf passed in as a url link.

#### get_urls(url: str) -> list:
Short function to isolate links from the chosen web page. As the webpage is pre-selected, they are all known to be pdf files.

    Args:
        url (string): the pre-selected web address.

    Return:
        pdfList(list): a Python list containing all the links extracted from the page. 
        
#### pdf_data_extract(url: str) -> dict:
Extracts text data from pdfs and passes it into a dictionary

    Args:
        url (string): a single url which must be a pdf file storage location.

    Return:
        clean_list (list): Python list containing corrected values from pdf text.

#### debug_problem_list(header_list:list, split_text: list) -> list:
Known data issues within the source pdfs are handled in this function

    Args:
        header_list (list): a list of the header data for the pdf
        split_text (list): a list of the core data 1.1-1.18, split by index

    Return:
        item_list (list): combined list of header data and the hygiened core data for the problem pdfs

