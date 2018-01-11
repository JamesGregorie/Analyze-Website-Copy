def soupfunc(input):
    r = requests.get(input)
    data = r.text
    soup = BeautifulSoup(data, 'html.parser')
    return soup

# grab links from the home page and add them into a list
def textscrape(website_frag):
    base_url = "http://www."+website_frag+".com"

    page_links = []
    page_set = []
    page_words = []

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
    for i in page_words:
        if len(i)<=3:
            page_words.remove(i)

    keyword_df[website_frag] = page_words

for i in website_frags:
    textscrape(i)

print(keyword_df)
