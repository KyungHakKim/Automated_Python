from newspaper import Article
import requests
import pandas as pd
from bs4 import BeautifulSoup

def make_urllist(page_num, code, date):
    urllist = []
    
    for i in range(1, page_num+1):
        url = 'https://news.daum.net/breakingnews/'+code+'?page='+str(page_num)+'&regDate='+str(date)
        
        news = requests.get(url)
        news.content
        
        soup = BeautifulSoup(news.content, 'html.parser')

        news_list = soup.select('.list_allnews li div strong')
        
        for line in news_list:
            urllist.append(line.a.get('href'))

    return urllist 

def make_data(urllist, code):
    text_list = []
    for url in urllist:
        article = Article(url, language='kp')
        article.download()
        article.parse()
        text_list.append(article.text)
        df = pd.DataFrame({'news' : text_list})
        df['news'] = df['news'].str.replace('\n',' ')
        df['code'] = idx2word[str(code)]
    return df

url_list = make_urllist(2, 'society', 20230103)
print('뉴스 기사의 개수 : ', len(url_list))
print(url_list[:5])

# # 파싱할 뉴스 기사 URL 지정
# url = 'https://v.daum.net/v/20230211141701492'

# # 언어를 한국어로 설정하고 URL을 전달해 Article 클래스의 객체 생성
# article = Article(url, language='ko')

# # 지정된 웹 페이지를 다운로드
# article.download()

# # 다운로드한 웹 페이지를 분석하고 필요한 정보를 추출
# article.parse()

# print('기사 제목 : ')
# print(article.title)

# print('기사 내용 : ')
# print(article.text)