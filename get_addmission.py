# coding=utf-8
import time
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By

def get_ad():
    username = "###########"
    password = "###########"
    driver = webdriver.Chrome()
    driver.get("https://#############")

    time.sleep(1)
    driver.find_element("xpath", """//*[@id="content"]/table/tbody/tr/td[1]/b/a""").click()

    time.sleep(1)
    driver.find_element("xpath", """//*[@id="email"]""").send_keys(username)

    time.sleep(1)
    driver.find_element("xpath", """//*[@id="password"]""").send_keys(password)

    time.sleep(2)
    driver.find_element("xpath", """//*[@id="content"]/form/table/tbody/tr/td[1]/div/button""").click()

    time.sleep(2)
    driver.find_element("xpath", """//*[@id="content"]/table/tbody/tr[3]/td[1]/div/a""").click()

    time.sleep(2)
    driver.find_element("xpath", """/html/body/div[4]/div/div/form/div[3]/button[1]""").click()

get_ad()