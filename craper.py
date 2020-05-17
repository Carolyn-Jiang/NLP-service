from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time


class web():
    def __init__(self,code):
        self.code = code

    def get_comment(self):
        driver = webdriver.Chrome("C:/Users/jiani/PycharmProjects/FInal/chromedriver.exe")
        url = 'https://finance.yahoo.com/quote/%s/community'% self.code
        driver.get(url)
        # search "Show More" button on the page, wait until find it and click it
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="canvass-0-CanvassApplet"]/div/button/span'))).click()
        # wait 4 sec after to load next 20 comments after press button
        # can decrease to 2 with good internet, increase to 10 with bad internet connection
        # YahooFinance default only load 20 comments, press showmore button can load 20 More
        # this proess repeat 4 times to get 100 comments, can add more times to fetch more commetns
        time.sleep(4)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="canvass-0-CanvassApplet"]/div/button/span'))).click()
        time.sleep(4)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="canvass-0-CanvassApplet"]/div/button/span'))).click()
        time.sleep(4)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="canvass-0-CanvassApplet"]/div/button/span'))).click()
        time.sleep(4)
        # search the text of comments by xpath
        comments = driver.find_elements_by_xpath(
            "//div[@class='C($c-fuji-grey-l) Mb(2px) Fz(14px) Lh(20px) Pend(8px)']")
        comments1 = [x.text for x in comments]
        return comments1
