import json
import sys
import time
import undetected_chromedriver

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

TESTING = 1

def get_data(url, category_name):
    # options and webdriver of our URL
    options = webdriver.ChromeOptions()
    # headless, we don't need it to actually show us the opened browser
    # options.add_argument('--headless')
    # incognito not to flood your browser history with parsed pages
    options.add_argument('--incognito')
    # create our driver using undetected_chromedriver to avoid antibot defense
    driver = undetected_chromedriver.Chrome(options=options)
    # the process of collecting data using selenium
    total_products_count = 0
    manufacturers = []
    print("[")
    try:
        driver.get(url)

        # for the while loop
        flag = True
        page_number = 1
        total_pages_count = -1
        while flag:
            time.sleep(3)
            if len(driver.find_elements(By.CLASS_NAME, 'listing-view-switcher__pointer--grid')) != 0:
                driver.execute_script("arguments[0].click();",
                                      driver.find_element(By.CLASS_NAME, "listing-view-switcher__button").find_element(
                                          By.CLASS_NAME, 'button'))
                time.sleep(1)
            if len(manufacturers) == 0:
                driver.execute_script("window.scrollBy(0,200)", "")
                boxes = driver.find_elements(By.CLASS_NAME, 'accordion__option')
                brand_box = -1
                for box in boxes:
                    if box.find_element(By.CLASS_NAME, 'accordion__title-text').text == 'Бренд':
                        brand_box = box
                        break
                to_click = brand_box.find_element(By.CLASS_NAME, 'show-all')
                if to_click.click() is None:
                    manufacturers = list(map(lambda x: x.text, brand_box.find_elements(By.CLASS_NAME, 'filter-name')))

            for i in range(6):
                driver.execute_script("window.scrollBy(0,1200)", "")
                time.sleep(1)

            if total_pages_count == -1:
                if len(driver.find_elements(By.CLASS_NAME, "page-link")) >= 2:
                    total_pages_count = int(driver.find_elements(By.CLASS_NAME, "page-link")[-2].text)

            total_products_count = parse_html(driver.page_source, "mvideo.ru", category_name, total_products_count,
                                              manufacturers)

            if page_number + 1 <= total_pages_count * TESTING:
                page_number += 1
                driver.get(url + "?page=" + str(page_number))
            else:
                # print('No next page')
                print("]")
                break
    except Exception as ex:
        print("]")
        # print(ex)
    finally:
        driver.close()
        driver.quit()


# Returns count of parsed products
def parse_html(src, url, category_name, total_products_count, manufacturers):
    soup = BeautifulSoup(src, "lxml")

    laptop_boxes = soup.find_all('div', class_='product-cards-layout__item ng-star-inserted')
    total_products_count = parse_group(laptop_boxes, url, category_name, total_products_count, manufacturers)

    laptop_boxes = soup.find_all('div', class_='product-cards-layout__item without-border ng-star-inserted')
    total_products_count = parse_group(laptop_boxes, url, category_name, total_products_count, manufacturers)
    return total_products_count


def parse_group(laptop_boxes, url, category_name, total_products_count, manufacturers):
    for laptop in laptop_boxes:
        try:
            name = laptop.find('div', class_='product-title product-title--list').a.text
            link = url + laptop.find('div', class_='product-title product-title--list').a.get('href')
            price = laptop.find('span', class_='price__main-value').text
            # price = laptop.find('span', class_='price__main-value').text
            pictures = list(map(lambda img: img.get('src'),
                                laptop.find_all('img', class_='product-picture__img product-picture__img--list')))
            product_info = {'name': name.strip(),
                            'url': "https://www." + link,
                            'cost': int(parse_price(price)),
                            'category': category_name,
                            'pictures': pictures,
                            'shop': 'М.Видео',
                            'manufacturer': determine_manufacturer(name, manufacturers),
                            }
            if total_products_count != 0:
                print(",", end="")
            total_products_count += 1
            print(json.dumps(product_info))
        except:
            continue
    return total_products_count


def parse_price(price):
    result = ""
    for c in price:
        if c.isdigit():
            result += c
    return result


def determine_manufacturer(name, manufacturers):
    for manufacturer in manufacturers:
        if manufacturer.lower() in name.lower():
            return manufacturer
    return ''


def main():
    # get_data('https://www.mvideo.ru/komputernye-aksessuary-24/myshi-183', 'myshi')
    arguments = sys.argv[1:]
    get_data(arguments[0], arguments[1])


if __name__ == "__main__":
    main()
