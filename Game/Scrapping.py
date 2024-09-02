########################################
#연습하기
########################################
import requests
from bs4 import BeautifulSoup

url = "https://www.ibksystem.co.kr/ir/history"

res = requests.get(url)

res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

# print(soup.a)
# print(soup.a.text)

target = soup.find( attrs={"class":"history-month"})
target2 = target.next_sibling


print(target)
print(target2)