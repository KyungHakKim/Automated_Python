import requests

url = 'https://iworld.ibksystem.co.kr/ekp/organization/organization.do?cmd=orgMainFrm&employee.searchField=byName&employee.orderBy=normal&employee.ascDesc=asc&employee.quickSearchYn=Y&employee.searchWord=%EC%A3%BC%EC%A7%84%EA%B7%9C'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0'}


response = requests.get(url, headers=headers)
html_Content = response.text 

print(response)