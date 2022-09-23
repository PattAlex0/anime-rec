def read_sitemap(sitemap, features):
    """ Identifies the urls and last modification date from sitemap
    
    arg:
        sitemap (BeautifulSoup): Should be a sitemap xml, created using BeautifulSoup
        features (list): The features in the sitemap that you want to read

    returns:
        sitePages (dictionary): Contains urls of site and when they were last modified

    """
    
    # Create empty dictionary
    sitePages = {}

    # Loop through features
    for feat in features:

        # Extract text from features
        feat_l = sitemap.find_all(feat)

        # Update dictionary with list of text
        sitePages.update( {feat: list(x.text for x in feat_l)} )

    # Return dictionary
    return sitePages


