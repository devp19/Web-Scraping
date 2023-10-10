'''
Webscraping Practice
Recent TLSA News from CNBC
GitHub: devp19
'''

import urllib.request
from bs4 import BeautifulSoup

class webScraper():
    def __init__(self, website):
        self.website = website
    
    def webScrape(self):
        
        article_count = 0
        results = []
        
        readSite = urllib.request.urlopen(self.website)
        html = readSite.read()
        parser = 'html.parser'
        sp = BeautifulSoup(html, parser)

        for tag in sp.find_all('a'):
            url = tag.get('href')
            if url is None:
                continue
            elif 'tesla' in url:
                
                if url not in results:
                    results.append(url)
                    article_count += 1
                    
                    if article_count >= 3:
                        break
        
        for link in results:
            print()
            print(link)
        print()

news = "https://www.cnbc.com/technology/"
webScraper(news).webScrape()