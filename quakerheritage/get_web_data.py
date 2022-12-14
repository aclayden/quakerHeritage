# quakerheritage/get_web_data.py

"""Main web function that collects url data and extracts text from each pdf examined.

This module allows the user to extract core data from formatted PDFs on the Britain Yearly Meeting website.

This module contains the following functions:

- `get_urls(url)` - Filters the Quaker Heritage Project's website for the url links to PDFs.
- `pdf_data_extract(url)` - Extracts core data text from a single pdf passed in as a url link.
"""

import io
import re

import bs4
import pdfplumber
import requests
import urllib3


def get_urls(url: str) -> list:
    """Helper function to isolate links from the chosen web page. As
    the webpage is pre-selected, they are all known to be PDF files.

    Parameters
    -----------
    url :class:`str`
        The pre-selected web address.

    Return a list containing all the links extracted from the page.
    """

    soup: bs4.BeautifulSoup = bs4.BeautifulSoup(
        markup=requests.get(url).text,
        features='html.parser',
        parse_only=bs4.SoupStrainer('a')
    )

    return [
        (url + link['href'])
        for link in soup
        if link.has_attr('href') and (link['href'][0] != '#')
    ]


def pdf_data_extract(url: str) -> dict:
    """Extracts text data from PDFs and passes it into a dictionary

    Parameters
    -----------
    url: :class:`str`
        A single URL to a PDF file storage location.

    Returns a dictionary containing the core data from the PDF as
    :class:`dict`.
    """

    http = urllib3.PoolManager()
    temp = io.BytesIO()
    temp.write(http.request("GET", url).data)
    pdf = pdfplumber.open(temp)
    all_text = ''

    header_list= pdf.pages[0].extract_text().splitlines()[0:5]
    header_data = [x.strip() for x in header_list if x.strip()]
    try:
        item_list = [url.split('/')[-1].split('.')[0].replace("%20", " "), header_data[0], header_data[1], header_data[2].split(': ')[1]]
    except IndexError: #Gildencroft PDF has a single line alteration from the usual formula that requires a string concatenation to resolve
        item_list = [url.split('/')[-1].split('.')[0].replace("%20", " "), header_data[0] + ' ' + header_data[1], header_data[2], header_data[3].split(': ')[1]]

    for pdf_page in pdf.pages:
        single_page_text = pdf_page.extract_text()
        if single_page_text is not None:
            all_text += '\n' + single_page_text
    split_text = re.split(r"[1]\.[0-9]+", all_text[all_text.find('1.1'):all_text.find('1.19')]) #From the full text, splits the section between 1.1-1.18 by the list index (e.g. 1.2, 1.15)
    try:
        for item in split_text[1:]:
            split_item = item.strip().split(': ')
            item_list.append(split_item[1].strip())
    except IndexError:
        original_headers = item_list[0:4]
        item_list = debug_problem_list(original_headers, split_text)
    clean_list = [item.replace('\n', '') for item in item_list]
    return clean_list


def debug_problem_list(header_list: list, split_text: list) -> list:
    """Fix known data issues within the source PDFs.

    Parameters
    -----------
    header_list: :class:`list`
        A list of the header data for the PDF.
    split_text: :class:`list`
        A list of the core data 1.1-1.18, separated by index.

    Returns the combined list of header data and hygiened core data for
    the problem PDFs as a :class:`list`.
    """

    cleaned_split_text = [
        item
            .replace(':  \n', ': Unknown \n')
            .replace(': \n', ': Unknown \n')
            .replace('- Cadw', ': Cadw')
        for item
        in [x for x in split_text if x.strip()]
    ]

    return header_list + [
        item.strip().split(': ')[1].strip()
        for item
        in cleaned_split_text
    ]
