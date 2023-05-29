# НЕ РАБОТАЕТ
# ВСЕ ЕЩЁ НЕ ОТКРЫВАЕТСЯ URL


import time
import undetected_chromedriver
import json

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


def check_exists_by_xpath(driver, xpath):
    try:
        driver.find_element(By.XPATH, xpath)
    except NoSuchElementException:
        return False
    return True


def get_data(url, category_name):
    # options and webdriver of our URL
    options = webdriver.ChromeOptions()
    # headless, we don't need it to actually show us the opened browser
    # options.add_argument('--headless')
    # incognito not to flood your browser history with parsed pages
    # options.add_argument('--incognito')
    # create our driver using undetected_chromedriver to avoid antibot defense
    driver = undetected_chromedriver.Chrome(options=options)
    # the process of collecting data using selenium
    total_products_count = 0
    try:
        driver.get(url)
        # for the while loop
        flag = True
        while flag == True:
            time.sleep(2)
            for i in range(4):
                driver.execute_script("window.scrollBy(0,1000)", "")
                time.sleep(1)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)

            total_products_count = parse_html(driver.page_source, "dns-shop.ru", category_name, total_products_count)
            # next page
            if check_exists_by_xpath(driver, "/html/body/div[2]/div/div[2]/div[2]/div[3]/div/div[5]/div/ul/li[11]/a"):
                element = driver.find_element(By.XPATH,
                                              "/html/body/div[2]/div/div[2]/div[2]/div[3]/div/div[5]/div/ul/li[11]/a")
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


def parse_html(src, url, category_name, total_products_count):
    soup = BeautifulSoup(src, "lxml")
    laptop_boxes = soup.find_all('div', class_='catalog-product ui-button-widget')
    for laptop in laptop_boxes:
        try:
            name = laptop.find('a', class_='catalog-product__name ui-link ui-link_black').span.string
            link = url + laptop.find('a', class_='catalog-product__name ui-link ui-link_black').get('href')
            price = laptop.find('div', class_='product-buy__price').text.strip().replace("₽", "")
            pictures = []
            product_info = {'name': name,
                            'link': link,
                            'cost': int(price.replace(" ", "")),
                            'category': category_name,
                            'pictures': pictures
                            }
            if total_products_count != 0:
                print(",", end="")
            total_products_count += 1
            print(json.dumps(product_info))
        except:
            continue
    return total_products_count


def main():
    get_data("https://www.dns-shop.ru/catalog/17a892f816404e77/noutbuki/", "noutbuki")


if __name__ == "__main__":
    main()
