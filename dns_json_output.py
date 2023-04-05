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
    #options.add_argument('--headless')
    #incognito not to flood your browser history with parsed pages 
    options.add_argument('--incognito')
    #create our driver using undetected_chromedriver to avoid antibot defense
    driver = undetected_chromedriver.Chrome(options=options)
    #the process of collecting data using selenium
    try:
        driver.get(url)
        #for the while loop
        flag= True
        while flag==True:
            time.sleep(2)
            for i in range(4):
                driver.execute_script("window.scrollBy(0,1000)","")
                time.sleep(1)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
            #write the html
            with open("index_selenium.html","w",encoding="utf-8") as file:
                file.write(driver.page_source)
            #parse html using beautiful soup
            id = parse_html("index_selenium.html","dns-shop.ru",outputname)
            #next page
            if check_exists_by_xpath(driver, "/html/body/div[2]/div/div[2]/div[2]/div[3]/div/div[5]/div/ul/li[11]/a"):  
                element = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div[2]/div[3]/div/div[5]/div/ul/li[11]/a")
                driver.execute_script('arguments[0].scrollIntoView();', element)
                driver.execute_script('window.scrollBy(0, -200);')
                element.click()
                time.sleep(2)
            else:
                print('No next page')
                flag = False
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()

def parse_html(filename,url,outputname):
    #get data using beautifulsoup
    with open(filename,"r",encoding="utf-8") as file:
        with open(outputname,"w",encoding= "utf-8") as json_file:
            src = file.read()
            #get data
            soup = BeautifulSoup(src,"lxml")
            laptop_boxes = soup.find_all('div',class_='catalog-product ui-button-widget')
            for laptop in laptop_boxes:
                try:
                    name = laptop.find('a',class_='catalog-product__name ui-link ui-link_black').span.string
                    link = url+laptop.find('a',class_ = 'catalog-product__name ui-link ui-link_black').get('href')
                    price = laptop.find('div',class_='product-buy__price').text.strip().replace("₽","")
                    productinfo = dict(name = name, link = link, price = price)
                    print(productinfo)
                    json.dump(productinfo, json_file, ensure_ascii=False, indent=4)
                except:
                    continue
    return


def main():
    get_data("https://www.dns-shop.ru/catalog/17a892f816404e77/noutbuki/","output.json")

if __name__ == "__main__":
    main()