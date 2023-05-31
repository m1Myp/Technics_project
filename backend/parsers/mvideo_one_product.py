import json
import sys
import time
import undetected_chromedriver

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

TESTING = 1


def get_data(url):
    # options and webdriver of our URL
    options = webdriver.ChromeOptions()
    # headless, we don't need it to actually show us the opened browser
    options.add_argument('--headless')
    # incognito not to flood your browser history with parsed pages
    # options.add_argument('--incognito')
    # create our driver using undetected_chromedriver to avoid antibot defense
    driver = undetected_chromedriver.Chrome(options=options)
    # the process of collecting data using selenium
    try:
        driver.get(url + '/shopdirections')
        time.sleep(2)
        driver.find_element(By.CLASS_NAME, 'location-text').click()
        for loc in driver.find_elements(By.CLASS_NAME, 'location-select__location'):
            if loc.text == "Новосибирск":
                loc.click()
        time.sleep(2)
        parse_html(driver.page_source)
    except Exception as ex:
        print("{}")
        # print(ex)
    finally:
        driver.close()
        driver.quit()


# Returns count of parsed products
def parse_html(src):
    soup = BeautifulSoup(src, "lxml")

    price = soup.find('span', class_='price__main-value').text
    availability = []
    shops_available = soup.find_all('div', class_='list-block__item ng-star-inserted')
    for shop in shops_available:
        try:
            shop_name = shop.find('span', class_='list-block__title-text').text
            shop_place = shop.find('div', class_='list-block__subtitle ng-star-inserted').text
            date = shop.find('div', class_='list-block__delivery').text
            availability.append({'shop_name': shop_name.strip(), 'shop_place': shop_place.strip(), 'date': date.strip()})
        except:
            continue
    product_info = {'cost': int(parse_price(price)), 'availability': availability}
    print(json.dumps(product_info))


def parse_price(price):
    result = ""
    for c in price:
        if c.isdigit():
            result += c
    return result


def main():
    # get_data('https://www.mvideo.ru/products/klaviatura-provodnaya-smartbuy-one-sbk-112u-k-50072271')
    arguments = sys.argv[1:]
    get_data(arguments[0])


if __name__ == "__main__":
    main()
