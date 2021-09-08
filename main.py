'''
Created on 2021. 9. 8.

@author: Innovationest
'''
import pyautogui as pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.alert import Alert
from datetime import datetime
import winsound
import time
import math

ID = input("아이디를 입력해주세요: ")
email = ID + "@gmail.com"
PW = input('비밀번호를 입력해주세요: ')

options = Options()
options.add_experimental_option('prefs', {
    "download.default_directory": "C:/Users/jajan/Documents/TopFundDownload",  # Change default directory for downloads
    "download.prompt_for_download": False,  # To auto download the file
    "download.directory_upgrade": True,
    "plugins.always_open_pdf_externally": True  # It will not show PDF directly in chrome
})
driver = webdriver.Chrome('C:\chromedriver.exe') #, options=options) # 해당 옵션은 다운로드 불가로 제외함

driver.maximize_window() # 대화면 크기

driver.get('https://www.topfund.kr/bbs/login.php')
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, '//*[@id="login_id"]')
    )
)
driver.find_element_by_xpath('//*[@id="login_id"]').send_keys(ID)
driver.find_element_by_xpath('//*[@id="login_pw"]').send_keys(PW)
driver.find_element_by_xpath('//*[@id="container"]/div[2]/form/div/div[1]/input').click()
time.sleep(0.5)
parent_window = driver.current_window_handle
for i in range(1, 15):
    driver.get('https://www.topfund.kr/mypage/investitems.php?&Lsst=&page='+ str(i) +'#dei')
    time.sleep(5)
    for j in range(1, 7):
        time.sleep(5)
        name = driver.find_element_by_xpath('//*[@id="container"]/div/div[1]/div[3]/div[2]/div['+ str(j) +']/p[2]')
        driver.find_element_by_xpath('//*[@id="container"]/div/div[1]/div[3]/div[2]/div['+ str(j) +']/a[2]').send_keys(Keys.ENTER)
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="info_table2"]/div[6]/img').click()
        all_windows = driver.window_handles
        for window in all_windows:
            if window != parent_window:
                child_window = window
        print(str(all_windows) +" :: " + str(parent_window) + " and " + str(child_window))
        time.sleep(25)
        print("자식 창으로 이동")
        driver.switch_to.window(child_window)
        time.sleep(5)
        print("프린트 활성")
        pyautogui.click(1050, 200)
        time.sleep(5)
        pyautogui.click(950, 920)
        time.sleep(5)
        driver.close()
        driver.switch_to.window(parent_window)
        time.sleep(5)
        # driver.find_element_by_xpath("/html/body/embed").click()
        # action = webdriver.ActionChains(driver).key_down(Keys.CONTROL).key_down("p").key_up("p").key_up(Keys.CONTROL)
        # driver.find_element_by_xpath("/html/body/embed").key_down(Keys.CONTROL)
        # driver.find_element_by_xpath("/html/body/embed").key_down("p")
        # driver.find_element_by_xpath("/html/body/embed").key_up("p")
        # driver.find_element_by_xpath("/html/body/embed").key_up(Keys.CONTROL)
        # #action.perform()
        # time.sleep(3)
        # print("프린트")
        # driver.find_element_by_xpath("/html/body/embed").send_keys(Keys.ENTER)

        # options = Options()
        # options.add_experimental_option('prefs', {
        #     "download.default_directory": "C:/Users/jajan/Documents/TopFundDownload",  # Change default directory for downloads
        #     "download.prompt_for_download": False,  # To auto download the file
        #     "download.directory_upgrade": True,
        #     "plugins.always_open_pdf_externally": True  # It will not show PDF directly in chrome
        # })
        # browser = webdriver.Chrome('C:\chromedriver.exe', options=options)
        # driver.
        # child_window = [window for window in all_windows if window != parent_window][0]
