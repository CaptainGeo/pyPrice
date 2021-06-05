#Author: CaptainGeo
#Date: 6-4-21
#Version: 1.0
from bs4 import BeautifulSoup
import requests
import json
import time

urls = [
    "https://coinmarketcap.com/currencies/bitcoin/",
    "https://coinmarketcap.com/currencies/cardano/",
    "https://coinmarketcap.com/currencies/dogecoin/"
]

for url in urls:
    coinMarketCap = requests.get(url)
    soup = BeautifulSoup(coinMarketCap.content, 'html.parser')

    data = soup.find('script',type="application/ld+json")
    coinData = json.loads(data.contents[0])
    for x in coinData:
        if x == 'currentExchangeRate':
            priceString = str(coinData[x]).strip('{}')
            priceInfo = priceString.split(',')
            price = float((priceInfo[1].split(':'))[1].strip())
    coin = coinData['name']
    slug = coinData['currency']
    print(coin + ' (' + slug + '): ' + "${:,.2f}".format(price))
