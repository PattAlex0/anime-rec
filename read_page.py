def read_page(url):
    """Scrapes the content from a URL. Taken from Practical Data Science (https://practicaldatascience.co.uk/data-science/how-to-scrape-and-parse-a-robotstxt-with-python).

    Args:
        url (string): The URL you want to scrape

    Returns:
        soup (string): HTML source
    """

    # Import libraries
    from urllib.request import urlopen, Request
    from bs4 import BeautifulSoup

    # Request url
    req = Request(url)

    # Open url
    opn = urlopen(req)

    # Get data
    soup = BeautifulSoup(opn, 'html.parser')

    # Return data
    return soup

