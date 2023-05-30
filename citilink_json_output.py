import requests
import time
import sqlite3
import os
import undetected_chromedriver
import json

from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

def check_exists_by_xpath(driver, xpath):
    try:
        driver.find_element(By.XPATH, xpath)
    except NoSuchElementException:
        return False
    return True


def get_data(url,outputname):
    #options and webdriver of our URL
    options = webdriver.ChromeOptions()
    #headless, we don't need it to actually show us the opened browser
    options.add_argument('--headless')
    #incognito not to flood your browser history with parsed pages 
    options.add_argument('--incognito')
    #create our driver using undetected_chromedriver to avoid antibot defense
    driver = undetected_chromedriver.Chrome(options=options)
    #the process of collecting data using selenium
    id = 0
    
    try:
        driver.get(url)
        #for the while loop
        flag= True
        pagenumber = 1
        while flag==True:
            time.sleep(2)
            for i in range(15):
                driver.execute_script("window.scrollBy(0,1200)","")
                time.sleep(1)
            driver.execute_script("window.scrollBy(0,-500);")
            time.sleep(2)
            #write the html
            with open("index_selenium.html","w",encoding="utf-8") as file:
                file.write(driver.page_source)
            #parse html using beautiful soup
            id = parse_html("index_selenium.html","citilink.ru",outputname,id)
            #next page
            if ((pagenumber <24) and (check_exists_by_xpath(driver, "/html/body/div[3]/div/main/section/div[2]/div/div/section/div[2]/div[3]/div/div[2]/a[1]"))):  
                element = driver.find_element(By.XPATH, "/html/body/div[3]/div/main/section/div[2]/div/div/section/div[2]/div[3]/div/div[2]/a[1]")
                driver.execute_script('arguments[0].scrollIntoView();', element)
                driver.execute_script('window.scrollBy(0, -200);')
                url = (str(url)).replace(str(pagenumber),str(pagenumber+1))
                driver.get(url)
                pagenumber= pagenumber+1
                time.sleep(2)
            else:
                print('No next page')
                flag = False
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()

def parse_html(filename,url,outputname,id):
    #get data using beautifulsoup
    with open(filename,"r",encoding="utf-8") as file:
        with open(outputname,"w",encoding= "utf-8") as json_file:
            src = file.read()
            #get data
            soup = BeautifulSoup(src,"lxml")
            laptop_boxes = soup.find_all('div',class_='e12wdlvo0 app-catalog-1bogmvw e1loosed0')
            for laptop in laptop_boxes:
                try:
                    id = id+1
                    name = laptop.find('div',class_='app-catalog-1tp0ino e1an64qs0').a.get('title')
                    link = url+laptop.find('div',class_ = 'app-catalog-1tp0ino e1an64qs0').a.get('href')
                    price = laptop.find('span',class_='e1j9birj0 e106ikdt0 app-catalog-j8h82j e1gjr6xo0').text
                    productinfo = dict(name = name, link = link, price = price,id = id)
                    #print(productinfo)
                    json.dump(productinfo, json_file, ensure_ascii=False, indent=4)
                except:
                    continue
    return id


def main():
    get_data("https://www.citilink.ru/catalog/noutbuki/?text=%D0%BD%D0%BE%D1%83&p=1","output.json")

if __name__ == "__main__":
    main()