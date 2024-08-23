import requests
from bs4 import BeautifulSoup


# headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0'}

# data = requests.get('http://www.google.com', headers=headers)
# data.raise_for_status()

# soup = BeautifulSoup(data.text, 'html.parser')
# print(soup)


html = '''
<html>
  <head>
    <title>온라인 쇼핑몰</title>
  </head>
  <body>
    <h1> 장바구니
      <p id='clothes' class='name' title='라운드티'> 라운드티 
        <span class = 'number'> 25 </span>
        <span class = 'price'> 29000 </span> 
        <span class = 'menu'> 의류</span>
        <a href = 'http://www.naver.com'> 바로가기 </a> 
      </p>
      <p id='watch' class='name' title='시계'> 시계 
        <span class = 'number'> 28 </span>
        <span class = 'price'> 32000 </span> 
        <span class = 'menu'> 액세서리 </span>
        <a href = 'http://www.facebook.com'> 바로가기 </a> 
      </p>
    </h1> 
  </body>
</html> 
'''

# BeautifulSoup 인스턴스 생성
soup = BeautifulSoup(html, 'html.parser')

pTag = soup.find_all('p')
# print(pTag)

idFind = soup.find_all(id='clothes')
# print(idFind)

spanFind = soup.find('p').find('span')
# print(spanFind)

soup.find('span', class_ = 'menu').get_text()
