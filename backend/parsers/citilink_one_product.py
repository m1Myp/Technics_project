import json
import sys
import time
import undetected_chromedriver

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

from parsers.citilink_catalog import solve_captcha

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
        driver.get(url)
        time.sleep(2)
        solve_captcha(driver)
        button = driver.find_element(By.CLASS_NAME, 'app-catalog-1iribqe')
        button.click()
        time.sleep(1)
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

    price = soup.find('span', class_='e1j9birj0 e106ikdt0 app-catalog-1f8xctp e1gjr6xo0').text
    availability = []
    shops_available = soup.find_all('div', class_='css-11xseab e10p0ntn0')
    for shop in shops_available:
        try:
            shop_name = shop.find('a', class_='css-afnr5f etc11sk0').text
            shop_place = shop.find('span', class_='e1ys5m360 e106ikdt0 css-v1w0m5 e1gjr6xo0').text
            date = shop.find('span', class_='e1ys5m360 e106ikdt0 css-g96g9y e1gjr6xo0').text.split(',')[0]
            availability.append(
                {'shop_name': shop_name.strip(), 'shop_place': shop_place.strip(), 'date': date.strip()})
        except:
            continue
    product_info = {'cost': int(parse_price(price)), 'availability': availability}
    # print(product_info)
    print(json.dumps(product_info))


def parse_price(price):
    result = ""
    for c in price:
        if c.isdigit():
            result += c
    return result


def main():
    # get_data(
    #     'https://www.citilink.ru/product/mysh-sunwind-sw-m715gw-igrovaya-lazernaya-besprovodnaya-usb-chernyi-hm-1422408/')
    arguments = sys.argv[1:]
    get_data(arguments[0])


if __name__ == "__main__":
    main()
