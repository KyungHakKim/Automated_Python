#나도 코딩 정규식 관련
import re


# . : 한 문자 (ca.e)
# ^ : 문자열의 시작 (^de) de로 시작하는 문자
# $ : 문자열의 끝. (se$) 


def print_match(m):
    if m:
        print("m.group() : ",m.group())
        print("m.string : ", m.string)
        print("m.start() : ", m.start())
        print("m.end() : ", m.end())
        print("m.span() : ", m.span())  #start end를 같이 표시
    else:
        print("매칭 되지 않음")

p = re.compile("ca.e")

m = p.match("case") #문자열 처음 부터 정규식과 일치하는지 검사
print_match(m)

m = p.search("good care")   #문자열의 중에 정규식과 일치하는 지 검사

lst = p.findall("careless is cafe")   #일치하는 모든 것을 리스트 형태로 반환
print(lst)