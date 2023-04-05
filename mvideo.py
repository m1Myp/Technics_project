import requests
import time
import sqlite3
import os
import undetected_chromedriver

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


def get_data(url):
    #options and webdriver of our URL
    options = webdriver.ChromeOptions()
    #headless, we don't need it to actually show us the opened browser
    options.add_argument('--headless')
    #incognito not to flood your browser history with parsed pages XD
    options.add_argument('--incognito')
    #create our driver using undetected_chromedriver to avoid antibot defense
    driver = undetected_chromedriver.Chrome(options=options)
    #the process of collecting data using selenium
    try:
        driver.get("https://www.mvideo.ru/noutbuki-planshety-komputery-8/noutbuki-118?reff=menu_main")
        flag = True
        #database for the data that we will scrape
        database = sqlite3.connect("products.db")
        # Create table
        database.execute('''CREATE TABLE IF NOT EXISTS laptops(id, name,link,price)''')
        #id for the database
        id = 0
        while flag == True:
            time.sleep(2)
            #scroll down by little bit to download full page
            for i in range(7):
                driver.execute_script("window.scrollBy(0,1000)","")
                time.sleep(1)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
            #write the html
            with open("index_selenium.html","w",encoding="utf-8") as file:
                file.write(driver.page_source)

            #parse html using beautiful soup
            id = parse_html("index_selenium.html","mvideo.ru",database,id)
            #next page
            if check_exists_by_xpath(driver, "/html/body/mvid-root/div/mvid-primary-layout/mvid-layout/div/main/mvid-plp/mvid-product-list-block/div[2]/mvid-pagination-controls/div[2]/mvid-plp-pagination/mvid-pagination/ul/li[10]/a"):
                element = driver.find_element(By.XPATH, "/html/body/mvid-root/div/mvid-primary-layout/mvid-layout/div/main/mvid-plp/mvid-product-list-block/div[2]/mvid-pagination-controls/div[2]/mvid-plp-pagination/mvid-pagination/ul/li[10]/a")
                driver.execute_script('arguments[0].scrollIntoView();', element)
                driver.execute_script('window.scrollBy(0, -200);')
                element.click()
                time.sleep(2)
            else:
                print('No next page!')
                flag = False
        database.close()
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()
    


def parse_html(filename,url,database,id):
    #get data using beautifulsoup
    with open(filename,"r",encoding="utf-8") as file:
        src = file.read()
        #get data
        soup = BeautifulSoup(src,"lxml")
        laptop_boxes_1 = soup.find_all('div',class_='product-cards-layout__item ng-star-inserted')
        laptop_boxes_2 = soup.find_all('div',class_='product-cards-layout__item without-border ng-star-inserted')
        for laptop in laptop_boxes_1:
            try:
                name = laptop.find('a',class_='product-title__text').text
                link = url+laptop.find('a',class_ = 'product-title__text').get('href')
                price = laptop.find('span',class_='price__main-value').text.strip().replace("₽","")
            except:
                continue
            #insert into the database
            data = [id,name,link,price]
            id = id + 1
            database.execute("INSERT INTO laptops VALUES(?,?,?,?)",data)
            database.commit()

            #print(name)
            #print(link)
            #print(price)
        for laptop in laptop_boxes_2:
            try:
                name = laptop.find('a',class_='product-title__text').text
                link = url+laptop.find('a',class_ = 'product-title__text').get('href')
                price = laptop.find('span',class_='price__main-value').text.strip().replace("₽","")
            except:
                continue
            #insert into the database
            data = [id,name,link,price]
            id = id + 1
            database.execute("INSERT INTO laptops VALUES(?,?,?,?)",data)
            database.commit()
            #print(name)
            #print(link)
            #print(price)
    return id 
            

    #we need to refresh the file each time
    os.remove("index_selenium.html")

def main():
    get_data("https://www.mvideo.ru/noutbuki-planshety-komputery-8/noutbuki-118?reff=menu_main")

if __name__ == "__main__":
    main()

