# -*- coding: utf-8 -*-
"""
Created on Fri May  6 14:45:27 2022

@author: Begear
"""


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import os

ACCOUNT_FOLDER = 'accounts'
ACCOUNT_TXT = 'credential.txt'

class Bot():
    def __init__(self, username, password):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get('https://www.instagram.com/')
        time.sleep(2)
        print('click')
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div/button[1]').click()
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input').send_keys(username)
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input').send_keys(password)
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]/button/div').click()
def main():
    with open(os.path.join(ACCOUNT_FOLDER, ACCOUNT_TXT)) as f:
        username, password = f.read().splitlines()
        
    my_bot = Bot(username, password)
    
if __name__ == '__main__':
    main()