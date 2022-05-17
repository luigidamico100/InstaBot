# -*- coding: utf-8 -*-
"""
Created on Fri May  6 14:45:27 2022

@author: luigidamico
"""


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import os
import pyautogui

ACCOUNT_FOLDER = 'accounts'
ACCOUNT_TXT = 'credential.txt'
IMAGES_FOLDER = 'images'

class HTMLBot():
    def __init__(self, username, password):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get('https://www.instagram.com/')
        time.sleep(2)
        print('click')
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div/button[1]').click()
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input').send_keys(username)
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input').send_keys(password)
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]/button/div').click()


class CVBot():
    def __init__(self, username, password):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get('https://www.instagram.com/')
        self.find_and_click(os.path.join(IMAGES_FOLDER, '1_cookies.png'))
        print('cookies ok')
        self.find_and_write(os.path.join(IMAGES_FOLDER, '2_username.png'), username)
        print('username ok')
        self.find_and_write(os.path.join(IMAGES_FOLDER, '2_password.png'), password)
        print('password ok')
        self.find_and_click(os.path.join(IMAGES_FOLDER, '2_login.png'))
        print('login ok')
        self.find_and_click(os.path.join(IMAGES_FOLDER, '3_1.png'))
        self.find_and_click(os.path.join(IMAGES_FOLDER, '3_2.png'))


    def find_and_click(self, image_path, confidence=0.8):
        while not pyautogui.locateOnScreen(image_path, confidence=.8):
            time.sleep(0.1)
        box = pyautogui.locateOnScreen(image_path, confidence=confidence)
        pyautogui.moveTo(box.left+(box.width/2), box.top+(box.height/2), .5)
        pyautogui.click()
        
        
    def find_and_write(self, image_path, string_to_write, interval=.1, confidence=0.8):
        while not pyautogui.locateOnScreen(image_path, confidence=.8):
            time.sleep(0.1)
        box = pyautogui.locateOnScreen(image_path, confidence=confidence)
        pyautogui.moveTo(box.left+(box.width/2), box.top+(box.height/2), .5)
        pyautogui.click()
        pyautogui.write(string_to_write, interval=interval)

        
def main():
    with open(os.path.join(ACCOUNT_FOLDER, ACCOUNT_TXT)) as f:
        username, password = f.read().splitlines()
        
    my_bot = CVBot(username, password)
    
if __name__ == '__main__':
    main()

    
    
