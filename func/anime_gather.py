def anime_gather(url):
    """Gathers TV animes with a score of at least 6.0 and puts them into a pandas dataframe.

    args:
        url: The base url for this function to loop over. Should correspond to a letter of the MAL catalogue

    returns:
        anime_df: the pandas dataframe
    """

    # Libraries
    import requests
    import re
    import pandas as pd
    from func.read_page import read_page

    # Set check to True and iterator to 0
    check = True
    iterator = 0

    # Create empty dataframe
    df_dict = {"episodes": [], 
               "rating": [], 
               "url": []}
    df_anime = pd.DataFrame(df_dict)

    # Loop while check is True
    while check:

        # Request page
        print("Checking page status")
        page = str(url + "&show=" + str(iterator))
        r = requests.get(page)

        # Check page status
        if r.status_code == 404: 
            print("Reached 404, stopping function")
            check = False
            break

        # Get page content
        print("Reading url for range " + str(iterator) + "-" + str(iterator+50))
        soup = read_page(url)

        # Create dataframe from table
        df = pd.DataFrame(pd.read_html(str(soup))[1])
        df = df.drop(0, axis = 1)
        df = df.drop(0)

        # Rename columns
        df = df.rename(columns = {1: "name", 2: "medium", 3: "episodes", 4: "rating", 5: "url"})

        # Gather urls from page
        urls_raw = soup.find(id = "content").find_all("a", class_ = "hoverinfo_trigger fw-b fl-l", href = True)
        df["url"] = [x['href'] for x in urls_raw]
        
        # Clean up names
        df["name"] = df["name"].apply(lambda x: re.sub(r"\sadd\s.*", "", x))

        # Set index
        df = df.set_index("name")

        # Filter to TV shows
        df = df[df["medium"] == "TV"]

        # Drop medium column
        df = df.drop("medium", axis = 1)

        # Filter to shows with a rating of more than 6.0
        df["rating"] = df["rating"].apply(float)
        df = df[df["rating"] >= 6.00]

        # Append to main dataframe
        df_anime = pd.concat([df_anime, df])

        # Add to iterator
        iterator += 50

    # Return dataframe 
    return df_anime
