#python -m venv myenv
#pip install pandas, selenium

#################################################
#Naver 시가 총액 크롤링 셀레니움 이용
#################################################
import os
import pandas as pd 
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.maximize_window()

url = 'https://finance.naver.com/sise/sise_market_sum.naver?&page='
browser.get(url)

#조회조건 초기화 하기
checkboxes = browser.find_elements(By.NAME, 'fieldIds')
for checkbox in checkboxes:
    if checkbox.is_selected():
        checkbox.click()
        
items_to_select = ['영업이익', '자산총계', '매출액' ]        


#조회조건에서 새로운 조건 선택하기
for checkbox in checkboxes:
    parent = checkbox.find_element(By.XPATH, '..') #부모 element 찾기
    label = parent.find_element(By.TAG_NAME, 'label')   #label이라는 하위 요소 찾기
    if label.text in items_to_select:
        checkbox.click()

#적용하기 버튼 클릭하여 조회하기    
btn_apply = browser.find_element(By.XPATH, '//a[@href="javascript:fieldSubmit()"]') #버튼을 xpath로 차는 방법
btn_apply.click()


#파일이 존재하면 삭제하
f_name = 'sise.csv'

if os.path.exists(f_name):
    os.remove(f_name)

#반복하며 크롤링 진행
for idx in range(1, 40):    #40페이지까지 수행
    #페이지 이동
    browser.get(url+str(idx))
    
    #데이터 추출
    df = pd.read_html(browser.page_source)[1] #두번째 list가 우리가 원하는 데이터임
    df.dropna(axis='index', how='all', inplace=True) #줄 전체가 비어있는 경우 줄 단위 삭제
    df.dropna(axis='columns', how='all', inplace=True) #컬럼 전체가 비어 있는 경우 컬럼 단위 삭제
    
    if len(df) == 0:
        break

    if os.path.exists(f_name):  #파일이 있으면 헤더 제외
        df.to_csv(f_name, encoding='utf-8-sig', index=False, mode='a', header=False)
    else:
        df.to_csv(f_name, encoding='utf-8-sig', index=False)

    print(f'{idx} 페이지 완료')
    
browser.quit()    