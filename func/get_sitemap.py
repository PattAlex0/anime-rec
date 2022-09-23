def get_sitemap(robots):
    """Gets site maps from robots text. Taken from Practical Data Science (https://practicaldatascience.co.uk/data-science/how-to-scrape-and-parse-a-robotstxt-with-python)

    args:
        robots (string): the robots text content you want to parse

    returns:
        maps_l (list): A list of all identified site maps
    """

    # Create empty list
    maps_l = []

    # Split lines in robots file
    lines = str(robots).splitlines()

    # Loop through lines
    for line in lines:

        # Check if line contains site map
        if line.startswith('Sitemap:'):
            
            # Split line by :
            split = line.split(':', maxsplit = 1)
            
            # Add the sitemap to maps list
            maps_l.append(split[1].strip())

    # Return maps list
    return maps_l
