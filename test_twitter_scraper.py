#%%
from  selenium import webdriver
from twitter_scraper_selenium import scrape_keyword
import pandas as pd
import asyncio
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
import requests
import pandas as pd
from bs4 import BeautifulSoup
import numpy as np
import json
    
# %%
# https://www.scrapingdog.com/blog/scrape-twitter/

from bs4 import BeautifulSoup
from selenium import webdriver
import time




l=list()
o={}

target_url = "https://twitter.com/barackobama"


driver=webdriver.Chrome()

driver.get(target_url)
time.sleep(20)

button = driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[1]/div/div/div/div[1]/div')
button.click();
time.sleep(1.3)

resp = driver.page_source
driver.close()

soup=BeautifulSoup(resp,'html.parser')

try:
    o["profile_name"]=soup.find("div",{"class":"r-1vr29t4"}).text
except:
    o["profile_name"]=None

try:
    o["profile_handle"]=soup.find("div",{"class":"r-1wvb978"}).text
except:
    o["profile_handle"]=None

try:
    o["profile_bio"]=soup.find("div",{"data-testid":"UserDescription"}).text
except:
    o["profile_bio"]=None

profile_header = soup.find("div",{"data-testid":"UserProfileHeader_Items"})

try:
    o["profile_category"]=profile_header.find("span",{"data-testid":"UserProfessionalCategory"}).text
except:
    o["profile_category"]=None

try:
    o["profile_website"]=profile_header.find('a').get('href')
except:
    o["profile_website"]=None

try:
    o["profile_joining_date"]=profile_header.find("span",{"data-testid":"UserJoinDate"}).text
except:
    o["profile_joining_date"]=None

try:
    o["profile_following"]=soup.find_all("a",{"class":"r-rjixqe"})[0].text
except:
    o["profile_following"]=None

try:
    o["profile_followers"]=soup.find_all("a",{"class":"r-rjixqe"})[1].text
except:
    o["profile_followers"]=None


l.append(o)

print(l)
# %%
from bs4 import BeautifulSoup
from selenium import webdriver
import time

url = 'https://twitter.com/search?q=Yellowknife%20(%23YellowKnife)%20until%3A2023-09-15%20since%3A2023-08-15&src=typed_query&f=live'

o = webdriver.ChromeOptions()
#provide location where chrome stores profiles
o.add_argument(r"--user-data-dir=/Users/samharris/Library/Application Support/Google/Chrome")
#provide the profile name with which we want to open browser
o.add_argument(r'--profile-directory=Profile 13')


driver = webdriver.Chrome(options=o)

driver.get(url)
time.sleep(15)

#button = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[2]/nav/a[2]/div')
#button.click();
#driver.close()
# %%
