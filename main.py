# My First Scraping using BeautifulSoup searching using multiple parameters & filtering results

import urllib3
from bs4 import BeautifulSoup

parameters = ['dildo', 'sofa']

for parameter in parameters:
    url = "https://london.craigslist.org/search/sss?query=" + parameter
    ourUrl = urllib3.PoolManager().request('GET', url).data
    soup = BeautifulSoup(ourUrl, "lxml")
    results = soup.findAll('a', attrs={'class': 'result-title hdrlnk'})

    for result in results:
        if "new" in result.text.lower():
            print(result.text)
            