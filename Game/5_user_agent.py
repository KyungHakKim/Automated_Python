#나도 코딩 웹스크래핑 강좌

import requests

headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0"}

url = "http://nadocoding.tistory.com"
res = requests.get(url,headers=headers)

res.raise_for_status()  #리스폰스가 에러이면 오류를 발생 시키는 메소드

#결과를 파일로 저장하는 방법
with open("nado.html","w", encoding="utf8") as f:
    f.write(res.text)
    