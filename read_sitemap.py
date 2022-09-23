def read_sitemap(sitemap):
    """ Identifies the urls and last modification date from sitemap
    
    arg:
        sitemap (BeautifulSoup): Should be a sitemap xml, created using BeautifulSoup

    returns:
        sitePages (dictionary): Contains urls of site and when they were last modified

    """

    # Get url list
    url_l = site_map.find_all("loc")
    url_l = [x.text for x in url_l]

    # Get lastmod
    lastmod_l = site_map.find_all("lastmod")
    lastmod_l = [x.text for x in lastmod_l]

    # Join in dictionary
    sitePages = {'url': url_l, 
                 'lastmod': lastmod_l}

    # Return dictionary
    return sitePages


