from bs4 import BeautifulSoup
import requests
import sys
import mysql.connector
from selenium import webdriver
# from helper import loadenvapi
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
# from database_helper import insert_bulk_data
import validators
import os
import json
# from selenium.webdriver.chrome.options import Options


# options = Options()
# options.headless = True

array_data=[]

if len(sys.argv)<2:
    print("Argumen tidak lengkap")
    # print(datetime.now().strftime("%d %B %Y %H:%M:%S"))
    exit()

# limit = os.getenv("LIMIT_ASYNC", 6)
# limit = int(limit)
search = sys.argv[1]

page = 'https://www.instagram.com/p/Cx5pSRNI0eC/'
# browserku=webdriver.Chrome(options=options)
# browserku.get(page)
# webdriverchek = browserku.page_source
webdriverchek = response = requests.get(page)
soup = BeautifulSoup(webdriverchek.text, "html.parser")
paging = soup.find("video")
# videoawal=paging.find
print(paging)
if paging == None:
    exit()
