import requests
from bs4 import BeautifulSoup
import re

# url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=5&rocketAll=false&searchIndexingToken=1=9&backgroundColor=4"
url = "https://www.coupang.com"
headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0"}

res = requests.get(url, headers=headers)

res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

print(res.text)
items = soup.find_all("li", attrs={"class" : re.compile("^search-product")})

print(items[0].find("div", attrs={"class":"name"}).get_text()) 