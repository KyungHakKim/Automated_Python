#################################################
#Naver 시가 총액 크롤링 requests이용
#################################################

import requests
from bs4 import BeautifulSoup
import pandas as pd
import os



# 데이터 저장
data = []
for idx in range(1,40):

    # URL 설정
    url = "https://finance.naver.com/sise/sise_market_sum.naver?&page=" + str(idx)

    # HTTP 요청
    response = requests.get(url)
    response.raise_for_status()  # 요청이 성공했는지 확인

    # HTML 파싱
    soup = BeautifulSoup(response.text, 'html.parser')

    # 테이블 데이터 추출
    table = soup.find('table', {'class': 'type_2'})
    rows = table.find_all('tr')

    print("processing... " + str(idx))
        
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip().replace("\r","").replace("\n","").replace("\t","") for ele in cols]

        if len(cols) > 1:  # 빈 행 제외
            data.append(cols)

# 데이터프레임 생성
columns = ['N', 'Name', 'Current Price', 'Change', 'Change Rate', 'Volume', 'Trading Value', 'Market Cap', 'Shares', 'Foreign Ratio', 'PER', 'ROE','토론']
df = pd.DataFrame(data, columns=columns)

print('End processing....')

#파일이 존재하면 삭제하
f_name = 'sise2.csv'

if os.path.exists(f_name):
    os.remove(f_name)

#df 파일에 저장하기
df.to_csv(f_name, encoding='utf-8-sig', index=False)