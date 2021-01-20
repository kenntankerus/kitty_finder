#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 21:35:45 2021

@author: kenn
"""

import time 
from bs4 import BeautifulSoup
from selenium import webdriver
from sms_alert import email_alert
from selenium.webdriver.firefox.options import Options

opt = Options()
opt.headless = True

url = 'https://www.sfspca.org/adoptions/cats/'
driver = webdriver.Firefox(options = opt)
cats = []
driver.get(url)
content = driver.page_source
soup = BeautifulSoup(content,features='lxml')
for cat in soup.findAll(attrs={'class':'adoption__item--name'}):
    cats.append(cat.text)

while True:
    driver.get(url)
    cats_temp = []
    content = driver.page_source
    soup = BeautifulSoup(content,features='lxml')
    for cat in soup.findAll(attrs={'class':'adoption__item--name'}):
        cats_temp.append(cat.text)
        if cat.text not in cats:
            title = 'Adopt %s!' % cat.text
            msg = 'Adopt %s! /n %s' % (cat.text, url)
            email_alert(title,msg,"6172797545@mms.cricketwireless.net")
            email_alert(title,msg,"kenntankerus@gmail.com")
            email_alert(title,msg,"6174477495@tmomail.net")
            email_alert(title,msg,"erich.tisch@gmail.com")
            email_alert(title,msg,"7815268338@tmomail.net")
            email_alert(title,msg,"alison.tisch@gmail.com")           
    if cats_temp:
        cats = cats_temp
        cats.sort()
    print(time.ctime(),':',cats)
    time.sleep(30)
