#나도 코딩 웹 스크래핑 beatifulSoup

import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/sise_market_sum.naver?&page="
res = requests.get(url)

res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

print(res.text)


    
#네이버 웹툰 전체 목록 가져오기
cartoons = soup.find_all("td",attr={"class":"title"})

link = cartoons[0].a["href"]    #엘리먼트에서 특정한 속성 데이터를 가져오기
#class 속성이 title인 모든
for cartoon in cartoons:
    print(cartoon.get_text())



