import pandas as pd
import requests
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/marketindex'

exchangeLists = pd.read_html(url, encoding='cp949')
# print(exchangeLists)

url = 'https://finance.naver.com/marketindex/exchangeList.naver'

exchangeLists2 = pd.read_html(url, encoding='cp949')


df = exchangeLists2[0]
# print(df)

currencyCode = 'USD'

currencyTuple = ('USD', 'JPY', 'EUR', 'CNY')

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0'}

currecnyValue = []
for currencyCode in currencyTuple:
    print(currencyCode)
    
    url = 'https://finance.naver.com/marketindex/exchangeDetail.naver?marketindexCd=FX_' + currencyCode + 'KRW'
    response = requests.get(url, headers=headers)
    html_Content = response.text 
    soup = BeautifulSoup(html_Content, 'html.parser')

    rateInfo = soup.find('p', class_='no_today').get_text().replace('\n','')
    print(rateInfo)
    
    currecnyValue.append(rateInfo)

currencyList = []
currencyList.append(list(currencyTuple))
currencyList.append (currecnyValue)

print(currencyList)

print(currencyList[0])
























