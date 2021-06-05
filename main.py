# selenium으로 키워드에 대한 네이버 뉴스 검색에서 각 언론사, 기사, 링크주소 크롤링
from selenium import webdriver
import time
import urllib

binary = 'c:/chromedriver/chromedriver.exe'   # 크롬드라이버 파일경로 입력
browser = webdriver.Chrome(binary)   # 브라우저를 인스턴스화
# 뉴스 검색 키워드 입력 및 해당 페이지 로드
keyword = input("검색할 뉴스를 입력하세요")
page = int(input("검색할 페이지를 입력하세요"))
browser.get("https://search.naver.com/search.naver?query="+keyword+"&where=news&ie=utf8&sm=nws_hty")

# 페이지별 언론사,기사제목,링크 수집하여 txt로 저장
file = open("d:\\data\\naver_news.txt","w")   # 텍스트 파일을 저장할 경로
for i in range(1, page+1):
    browser.find_element_by_link_text(str(i)).click()   # 링크가 있는 태그의 텍스트로 찾아서 페이지 클릭
    time.sleep(3)
    press = browser.find_elements_by_css_selector('a.press')   # 태그와 클래스로 추출
    title = browser.find_elements_by_css_selector('a.news_tit')
    for i, j in zip(press,title):
        file.write(i.text+'\t'+j.text+'\t'+j.get_attribute('href')+'\n')   # 텍스트 파일에 저장
file.close()

# 브라우저 종료
browser.quit()