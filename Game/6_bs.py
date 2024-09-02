#나도 코딩 웹 스크래핑 beatifulSoup

import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon"
res = requests.get(url)

res.raise_for_status()



soup = BeautifulSoup(res.text, "lxml")


###태그로 속성 찾기
print(soup.a) #첫번째로 발견된 a태크

# print(soup)
# print(soup.a.attrs)   #a엘리먼트의 속성 정보
# print(soup.a["href"]) #a속성 값의 실제 값

print(soup.find("a", attrs={"class":"Nbtn_upload"}))   #a테그에서 클래스명 일치하는 엘리먼트 찾기
print(soup.find(attrs={"class":"Nbtn_upload"}))         #전체에서 클래스명 일치하는 엘리먼트 찾기

rank1 = soup.find("li", attrs={"class":"rank01"})   #rank01 클랙스 찾기
print(rank1.a.get_text())

##XPath로 속성 찾기
print(rank1.next_sibling) #다음 형제 속성 찾기
rank2 = rank1.next_sibling.next_sibling

rank1 = rank2.previous_sibling  #이전 형제 속성 찾기
rank1.parent        #부모 속성
rank1.find_next_sibling("li")   #li인 다음 형제 속성 찾기. 중간에 개행 등 다른 속성이 있을 수 있음  
rank2.find_previous_sibling

rank1.find_next_siblings    #형제 속성을 모두 가져온다.
webtoon = soup.find("a", text="찾고자 하는 텍스트") # a 태그에서 텍스트가 일치하는 속성 찾기