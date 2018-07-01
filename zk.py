from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

browser = webdriver.Chrome()

def get_page():

    try:

        browser.get('http://jw.zhku.edu.cn/')
        # input_3 = WebDriverWait(browser, 20).until(
        #     EC.presence_of_element_located((By.CSS_SELECTOR, "#Logon > table > tbody > tr:nth-child(1) > td > table > tbody > tr:nth-child(2) > td:nth-child(2) > select")))
        # id=WebDriverWait(browser,10).until(EC.element_located_selection_state_to_be((By.CSS_SELECTOR,'#Logon > table > tbody > tr:nth-child(1) > td > table > tbody > tr:nth-child(2) > td:nth-child(2) > select > option:nth-child(2)')))
        input = WebDriverWait(browser, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "#txt_asmcdefsddsd")))
        # input_2 = WebDriverWait(browser, 4).until(
        #         EC.presence_of_element_located((By.CSS_SELECTOR, "#txt_pewerwedsdfsdff")))

        # submit=WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, 'someid')))
        input.send_keys('201520124223')#输入id
        # input_2=browser.find_element_by_id('txt_pewerwedsdfsdff')
        # input_2.send_keys('312368')

    except TimeoutException:
        return get_page()
if __name__=='__main__':
    get_page()
# input_3=browser.find_element_by_id('txt_sdertfgsadscxcadsads')
# input_3.send_keys('')#输入返回的验证码
# button=browser.find_element_by_id('su')#搜索确认键
# button.click()
 #完成登陆
