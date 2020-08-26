from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup



# # ID. PWD 변수 입력
# print("E학습터 아이디를 입력해주세요.")
# id = input()
# print("E학습터 비밀번호를 입력해주세요.")
# pw = input()
id = "boyoungbk"
pw = "rlaqhdud1990!@"
xpath ='//*[@id="main_cont"]/li[2]/div[2]/ul/li[1]/a[2]'
class_name = "2020 서울신도초등학교 6학년 8반"
#javascript:enterClass(230655)

# 브라우저 설정
options = webdriver.ChromeOptions()
options.add_argument("disable-gpu")   # 가속 사용 x
options.add_argument("lang=ko_KR")    # 가짜 플러그인 탑재
options.add_argument("user_agent = Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36")
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






