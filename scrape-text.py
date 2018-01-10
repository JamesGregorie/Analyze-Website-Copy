import requests
import random
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup

website_frag = 'swiftprotech'

base_url = "http://www."+website_frag+".com"

page_links = []
page_set = [] #this is a set so we don't comb through pages twice
page_words = []


def soupfunc(input):
    r = requests.get(input)
    data = r.text
    soup = BeautifulSoup(data, 'html.parser')

# grab links from the home page and add them into a list
r = requests.get(base_url)
data = r.text
soup = BeautifulSoup(data, 'html.parser')
links = soup.find_all('a')
for a in links:
    try:
        if website_frag in a['href']:
            page_links.append(a['href'])
        elif a['href'].startswith('/'):
            page_links.append(base_url+a['href'])
    except:
        pass

# # #  go through the list generated from the home page and find the links from those pages.
for page in set(page_links):
    r = requests.get(page)
    data = r.text
    soup = BeautifulSoup(data, 'html.parser')
    links = soup.find_all('a')
    for a in links:
        try:
            if website_frag in a['href']:
                page_set.append(a['href'])
            elif a['href'].startswith('/'):
                page_set.append(base_url+a['href'])
            else:
                pass
        except:
            pass
print(page_set)

def get_words(iterable):
     for item in iterable:
            r = requests.get(page)
            data = r.text
            soup = BeautifulSoup(data, 'html.parser')
            txt = soup.find_all('p')
            for i in txt:
                words = (i.text.split(" "))
            for values in words:
                page_words.append((item, values))

get_words(set(page_set))
get_words(set(page_links))

for i in page_words:
    if len(i)<=3:
        page_words.remove(i)

df = pd.DataFrame(page_words)
df['count'] = df[1].apply(len)
clean_df = df[df['count']>4]
clean_df.groupby([1]).count().sort_values(['count'], ascending=False).head(15)
