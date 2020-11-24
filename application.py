"""boss直聘自动打招呼机器人"""

import requests
import time
from selenium import webdriver
import pickle
import os
from selenium.webdriver import ActionChains

geckodriver_path = r'D:\development\chromedriver_win32\geckodriver.exe'


def start(driver):
    driver.set_page_load_timeout(60)
    driver.set_script_timeout(60)  # 这两种设置都进行才有效
    time.sleep(10)
    print(driver.page_source)
    print("==========================================")
    jobsList = driver.find_elements_by_class_name("info-primary")
    for item in jobsList:
        time.sleep(5)
        link = item.find_element_by_tag_name("a")
        print(link.text)
        a = link.get_attribute('href')

        # 新开一个窗口，通过执行js来新开一个窗口
        js = 'window.open("%s");' % a
        driver.execute_script(js)

        # 输出当前窗口句柄（招聘信息列表）
        list_handle = driver.current_window_handle
        # 获取当前窗口句柄集合（列表类型）
        handles = driver.window_handles

        driver.switch_to_window(handles[1])

        driver.set_page_load_timeout(60)
        driver.set_script_timeout(60)  # 这两种设置都进行才有效
        time.sleep(20)
        print(driver.page_source)

        try:
            clink = driver.find_element_by_link_text("立即沟通")
            if clink != None:
                clink.click()
                print("已发送打招呼")
                time.sleep(5)

            driver.close()
            # 切换回百度窗口
            driver.switch_to.window(list_handle)

            time.sleep(5)
        except Exception as e:
            print(e)
            time.sleep(30)
            print("程序休息30秒")
            try:
                clink = driver.find_element_by_link_text("立即沟通")
                tx = clink.text
                print(tx)
                if clink != None:
                    clink.click()
                    print("已发送打招呼")
                    time.sleep(10)
            except:
                print("跳过该招聘信息")

            driver.close()
            # 切换回百度窗口
            driver.switch_to.window(list_handle)

            time.sleep(5)

if __name__ == '__main__':
    driver = webdriver.Firefox(executable_path=geckodriver_path)
    driver.set_page_load_timeout(60)
    driver.set_script_timeout(60)  # 这两种设置都进行才有效
    driver.get("https://login.zhipin.com/")
    usernameDiv = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[2]/div[2]')
    usernameDiv.click()
    time.sleep(16)
    driver.get('https://www.zhipin.com/job_detail/?query=Java&city=101280100&industry=&position=')
    driver.get('https://www.zhipin.com/job_detail/?query=Java&city=101280100&industry=&position=')
    time.sleep(15)

    print(driver.get_cookies())
    print("==========================================")



   # start(driver)


    for i in range(1,10):
        nextButton = driver.find_element_by_class_name("next")
        nextButton.click()

        start(driver)


