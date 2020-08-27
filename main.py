import calendar
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


# # ID. PWD 변수 입력
# print("E학습터 아이디를 입력해주세요.")
# id = input()
# print("E학습터 비밀번호를 입력해주세요.")
# pw = input()
id = "boyoungbk"
pw = "rlaqhdud1990!@"
class_name = "(부담임)2020 서울신도초등학교 6학년 8반"
data_list = {}

# 요일 구하는 함수
yyyy = 2020
mm = 8
dd = 26
day = calendar.weekday(yyyy, mm, dd)
day_list = ["월", "화", "수", "목", "금", "토", "일"]
date = "{}월 {}일 ({})".format(mm, dd, day_list[day])

# 브라우저 설정
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36"
options = webdriver.ChromeOptions()
options.add_argument("disable-gpu")   # 가속 사용 x
options.add_argument("lang=ko_KR")    # 가짜 플러그인 탑재
# options.add_argument("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36")
URL = "E:\worksp\chromedriver.exe"
browser = webdriver.Chrome(URL, options=options)
browser.get("https://cls1.edunet.net/cyber/cm/mcom/pmco000b00.do")
browser.implicitly_wait(1)

# 자바스크립트로 위장 클릭
def over_click(name):
    element = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.CLASS_NAME, name)))
    browser.execute_script("arguments[0].click();", element)

# 로그인하기
over_click("btn_login")
browser.find_element_by_class_name("dd_1").click()
browser.find_element_by_id("login_id").send_keys(id)
browser.find_element_by_id("password").send_keys(pw)
browser.implicitly_wait(1)
browser.find_element_by_class_name("doLogin").send_keys(Keys.ENTER)
browser.implicitly_wait(1)

# 학급으로 들어가기
browser.find_element_by_link_text(class_name).click()

# 학습현황체크 (1day)
browser.find_element_by_class_name("cu_list").click()
select = Select(browser.find_element_by_id("selectClssCrse"))
select.select_by_visible_text(date)

# 진도율 크롤링
name_list = []
progress_list = []
progress = browser.find_elements_by_class_name("percent")
for percent in progress:
    progress_list.append(percent.text.split('\n'))
progress_list = progress_list[:-5]

# 마지막 페이지 구하기
pages = browser.find_element_by_class_name("pagination")
print()

def save_csv():
    file = open("{}.csv".format(date), mode="w")
    writer = csv.writer(file)
    row_list = ["이름"] + ["{}".format(date)]
    writer.writerow(row_list)
    for
    print(file)

#아이디별 스크리핑