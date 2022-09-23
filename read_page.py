def read_page(url, parse = 'html.parser'):
    """Scrapes the content from a URL. Taken from Practical Data Science (https://practicaldatascience.co.uk/data-science/how-to-scrape-and-parse-a-robotstxt-with-python).

    Args:
        url (string): The URL you want to scrape
        parse (string): The content of the url that you want to parse. Function imports lxml to allow for xml parsing

    Returns:
        soup (string): HTML source
    """

    # Import libraries
    from urllib.request import urlopen, Request
    from bs4 import BeautifulSoup
    import lxml

    # Request url
    req = Request(url)

    # Open url
    opn = urlopen(req)

    # Get data
    soup = BeautifulSoup(opn, parse)

    # Return data
    return soup

