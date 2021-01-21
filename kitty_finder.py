#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 21:35:45 2021

@author: kenn
"""
# import libraries
import time 
import smtplib
from bs4 import BeautifulSoup
from selenium import webdriver
from email.message import EmailMessage
from selenium.webdriver.firefox.options import Options

# create function for sending an email message
def email_alert(subject, body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg["subject"] = subject
    msg["to"] = to
    
    ## this is the email address from which you wish to send kitten alerts
    user = "<your.email>@gmail.com"
    msg['from'] = user
    
    ## this password is a one-time setup via your gmail account (see link)
    password = "<gmail application password>"
    
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user,password)
    server.send_message(msg)
    server.quit()

# set options for browser True -> performs web scraping w/o opening window
opt = Options()
opt.headless = True

# where the kitties at?
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
            # cell provider email for tmobile <your.number>@tmomail.net
            email_alert(title,msg,"6174477495@tmomail.net")
            email_alert(title,msg,"7815268338@tmomail.net")
            # or just use a regular email address 
            email_alert(title,msg,"erich.tisch@gmail.com")
            email_alert(title,msg,"alison.tisch@gmail.com")           
    if cats_temp:
        cats = cats_temp
        cats.sort()
    print(time.ctime(),':',cats)
    time.sleep(30)