import requests
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup



website_frags = ['swiftprotech']
keyword_df = pd.DataFrame()

# Create function for basic BeautifulSoup HTML import
def soupfunc(input):
    r = requests.get(input)
    data = r.text
    soup = BeautifulSoup(data, 'html.parser')
    return soup

# Create function to scrape website for information
def textscrape(website_frag):
# Establish some empty variables and lists we will populate later
    base_url = "http://www."+website_frag+".com"

    page_links = []
    page_set = []
    page_words = []

# First operation is to scrape the homepage for links to other pages.
# Because pages are formated differently, the try/except statement helps to
#       negate some of the oddly formatted page_links
# Additionally, many pages, especially those formatted on WordPress Additionally
#       use the URL slug for their href. The elif statement handles these and
#       ultimately returns the completed URL

    soup = soupfunc(base_url)
    links = soup.find_all('a')
    for item in links:
        try:
            if 'http' in item['href']:
                page_links.append(item['href'])
            elif item.startswith('/'):
                page_links.append(base_url + item[href])
            else:
                pass
        except:
            pass

# We then use the links scraped above to broaded our search for readable text
# This script turns [page_links] into a set to avoid double counting page_set
# It then looks at those pages for any body copy in the <p> tags
# This is then read, broken in to individual words, and stored in a list
    for item in set(page_links):
        try:
            soup = soupfunc(item)
            txt = soup.find_all('p')
            for i in txt:
                words = (i.text.split(" "))
            for values in words:
                page_words.append(values)
        except:
            pass
# We want to gain insights into what words the website is focusing on
# This short line of code goes ahead and removes any words less than 4 characters long
#       which includes useless words such as "the, of, or, but, etc." leaving behind
#       longer, more insightful words
    for i in page_words:
        if len(i)<=3:
            page_words.remove(i)
# Lastly, the text is taken from the list and added in to a dataframe titled after the page it came from.
    keyword_df[website_frag] = page_words

for i in website_frags:
    textscrape(i)

print(keyword_df)
