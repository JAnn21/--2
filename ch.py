from bs4 import BeautifulSoup
import pandas as pd
import datetime
import urllib.request
from itertools import count
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import matplotlib as mpl
import matplotlib.pyplot as plt
import time
import ssl
import csv

driver = webdriver.Chrome('./chromedriver.exe')
driver.get('https://www.wadiz.kr/web/wreward/main?keyword=&endYn=ALL&order=recommend')


time.sleep(5)
endk = 5
while endk:
    driver.find_element_by_tag_name('body').send_keys(Keys.END)
    time.sleep(0.3)
    endk -= 1

page = driver.page_source

soup = BeautifulSoup(page,'html.parser')

time.sleep(2)

all_title = soup.find_all('strong')
title = [soup.find_all('strong')[n].string for n in range(0,len(all_title))]

all_tag = soup.find_all('span','RewardProjectCard_category__1vo_V')
tag = [soup.find_all('span','RewardProjectCard_category__1vo_V')[n].string for n in range(0,len(all_title))]

all_goal = soup.find_all('span','RewardProjectCard_percent__edRT9')
goal = [soup.find_all('span','RewardProjectCard_percent__edRT9')[n].string for n in range(0,len(all_title))]


all_price = soup.find_all('span','RewardProjectCard_amount__2GV5X')
price = [soup.find_all('span','RewardProjectCard_amount__2GV5X')[n].string for n in range(0,len(all_title))]


all_time = soup.find_all('span','RewardProjectCard_remainingDay__2KYop')
time = [soup.find_all('span','RewardProjectCard_remainingDay__2KYop')[n].string for n in range(0,len(all_title))]

for num in range(0,len(all_title)):
    goal[num] = goal[num].replace('%','')
    price[num] = price[num].replace('원','')
    price[num] = price[num].replace(',','')
    time[num] = time[num].replace('일','')
    time[num] = time[num].replace('오늘마감','0')
    goal[num] = int(goal[num])
    price[num] = int(price[num])
    time[num] = int(time[num])

test_list = []

for i in range(0,len(all_title)):
    roww = []
    roww.append(title[i])
    roww.append(tag[i])
    roww.append(goal[i])
    roww.append(price[i])
    roww.append(time[i])
    test_list.append(roww)			
    

csvfile = open("./wadiz.csv","w",newline="")
csvwriter = csv.writer(csvfile)
for row in test_list:
    csvwriter.writerow(row)
csvfile.close()
