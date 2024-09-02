#나도 코딩 웹스크래핑 강좌

import requests

url = "http://www.google.com"
res = requests.get(url)


# if res.status_code == requests.codes.ok:
#     print("정상")
# else:
#     print("오류 : ", res.status_code)

res.raise_for_status()  #리스폰스가 에러이면 오류를 발생 시키는 메소드

print(res.text)

#결과를 파일로 저장하는 방법
with open("mygoogle.html","w", encoding="utf8") as f:
    f.write(res.text)
    