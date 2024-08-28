import pandas as pd
import matplotlib.pyplot as plt
import requests
from datetime import datetime
from matplotlib import dates as mdates
from bs4 import BeautifulSoup as bs

url = 'https://finance.naver.com/item/sise_day.nhn?code=068270&page=1'
headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36'}
response = requests.get(url, headers=headers)

print(response.text)

html = bs(response.text, 'html.parser')
html_table = html.select("table")
table = pd.read_html(str(html_table))
print('파싱된 테이블의 개수 :', len(table))

# print(table[0].dropna())




df = pd.DataFrame()
stockCode = '068270'
sise_url = 'https://finance.naver.com/item/sise_day.nhn?code=' + stockCode
for page in range(1, 100):
    page_url = '{}&page={}'.format(sise_url, page)
    # print(page_url)

    # 위에서 했던 일련의 과정들을 각 url에 대해서 (99페이지에 대해서 반복)
    response = requests.get(page_url, headers=headers)
    html = bs(response.text, 'html.parser')
    html_table = html.select("table")
    table = pd.read_html(str(html_table))

    
    # 현재 얻은 데이터프레임을 기존 데이터프레임에 누적.
    # df = df.append(table[0].dropna()) #
    df = pd.concat([df,table[0].dropna()])
    
print(df)

