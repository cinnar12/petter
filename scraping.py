from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import csv

html_list = ["pages/dog1.html", "pages/dog2.html", "pages/cat1.html", "pages/cat2.html"]
pet_list = []

def get_pet_pages(bsObj):
    pet_links = bsObj.findAll("a")
    for link in pet_links:
        pet = link.attrs['href']
        pet_list.append(pet)

def get_pet_info(pet_list):
    for link in pet_list:
        html2 = urlopen(link)
        bsObj2 = BeautifulSoup(html2, "html.parser")
        try:
            pet_id = bsObj2.find("h1").get_text()
            pet_name = bsObj2.find("div", {"class":"price"}).get_text()
            pet_breed = bsObj2.find("div", {"class":"row"}).select("div > a")[0].get_text()
            pet_sex = bsObj2.find("div", {"class":"row"}).select("div > a")[1].get_text()
            pet_age = bsObj2.find("div", {"class":"row"}).select("div > a")[2].get_text()
            pet_weight = bsObj2.find("div", {"class":"row"}).select("div > a")[3].get_text()
            pet_location = bsObj2.find("div", {"class":"row"}).select("div > a")[4].get_text()
            pet_info = bsObj2.find("p", {"class":"p-style2"}).get_text()
        except:
            pet_id = "None"
            pet_name = "None"
            pet_breed = "None"
            pet_sex = "None"
            pet_age = "None"
            pet_weight = "None"
            pet_location = "None"
            pet_info = "None"
        pet_details = [pet_id, pet_name, pet_breed, pet_sex, pet_age, pet_weight, pet_location, pet_info]
        return pet_details
        time.sleep(2)

def write_csv(pet_list):
    csvFile = open("pets.csv", "w", encoding='utf-8')
    c = csv.writer(csvFile)
    c.writerow(["ID","Name","Breed", "Sex", "Age", "Weight", "Location","Info", "URL", "Image"])
    try:
        for pet in pet_list:
            var = get_pet_info(i)
            var.append("https://www.shelterluv.com/publish_animal/" + var[0])
            var.append("img/profile/" + var[1] + "-1.png")
            c.writerow(var)
            time.sleep(1)
    finally:
        csvFile.close()

for i in html_list:
    html = open(i)
    bsObj = BeautifulSoup(html, "html.parser")
    get_pet_pages(bsObj)
write_csv(pet_list)
