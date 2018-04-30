from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import csv

#csvFile = open("dogs.csv", "w", encoding='utf-8')
#c = csv.writer(csvFile)
#c.writerow(["Name","Breed", "Sex", "Age", "Weight", "Location","ID"])

html = open("pages/dog1.html")
bsObj = BeautifulSoup(html, "html.parser")
dog_list = []

def get_dog_pages(bsObj):
    dog_links = bsObj.findAll("a")
    print(dog_links)
    for link in dog_links:
        dog = link.attrs['href']
        print(dog)
        #dog_list.append(dog)

test_list= ["https://www.shelterluv.com/publish_animal/GPR-A-5254",
"https://www.shelterluv.com/publish_animal/GPR-A-5255",
"https://www.shelterluv.com/publish_animal/GPR-A-5256",
"https://www.shelterluv.com/publish_animal/GPR-A-5276",
"https://www.shelterluv.com/publish_animal/GPR-A-5275",
"https://www.shelterluv.com/publish_animal/GPR-A-5273"
]

def get_dog_info(test_list):
    for link in test_list:
        html2 = urlopen(link)
        bsObj2 = BeautifulSoup(html, "html.parser")
        dog_name = bsObj.find("div", {"class":"price"})
        print(dog_name)

#get_dog_pages(bsObj)
get_dog_info(test_list)
