"""
날짜 : 2023/01/17
이름 : 박가영
내용 : 파이썬 기상청 날씨 크롤링 실습하기
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pymysql

# 가상 브라우저 실행
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
browser = webdriver.Chrome('./chromedriver.exe', options=chrome_options)

# 페이지 이동
browser.get('https://www.weather.go.kr/w/obs-climate/land/city-obs.do')

# 데이터베이스 접속
conn = pymysql.connect(host='127.0.0.1', 
                user='root', 
                password='1234', 
                db='java2db', 
                charset='utf8')

cur = conn.cursor()

sql = "insert into `weather` values ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}', NOW())"

# 지역명 출력
trs = browser.find_elements(By.CSS_SELECTOR, '#weather_table > tbody > tr')

cols = []

for tr in trs:
    tds = tr.find_elements(By.CSS_SELECTOR, 'td')
    col1 = tds[0].find_element(By.CSS_SELECTOR, 'a').text
    for td in tds:
        cols = td.text.replace("&nbsp;", "")
    cur.execute(sql.format(col1, cols[1], tds[2], int(cols[3]), int(tds[4]), float(tds[5]), float(tds[6]), float(tds[7]), float(cols[8]), float(cols[9]), int(tds[10]), tds[11], float(tds[12]), float(tds[13])))
    conn.commit()

# 가상 브라우저 종료
conn.close()
browser.close()