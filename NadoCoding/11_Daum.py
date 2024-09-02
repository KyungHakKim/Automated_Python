import requests
from bs4 import BeautifulSoup
import os

def scrape_naver_finance_news():
    url = "https://finance.naver.com/news/mainnews.naver"
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.content, 'html.parser')
    news_titles = soup.select(".mainNewsList li a")


    with open("mygoogle.html","w", encoding="utf8") as f:
        f.write(str(response.text))
    
 
    # for title in news_titles:
    #     print(title.text)

if __name__ == "__main__":
    scrape_naver_finance_news()