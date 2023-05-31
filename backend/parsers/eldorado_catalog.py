import json
import sys
import time
import undetected_chromedriver

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

# Set this variable to 0 if you want to parse just one page, otherwise set it to 1
TESTING = 1


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
    manufacturers = []
    print("[")
    try:
        driver.get(url)
        # time.sleep(5)
        # url = url + '/?m=ONLY_AVAILABLE'
        # driver.get(url)

        # for the while loop
        flag = True
        page_number = 1
        total_pages_count = -1
        while flag:
            time.sleep(5)

            if len(manufacturers) == 0:
                driver.execute_script("window.scrollBy(0,1000)", "")
                boxes = driver.find_elements(By.TAG_NAME, 'div')
                brand_box = -1
                for box in boxes:
                    try:
                        if box.find_element(By.TAG_NAME, 'div').get_attribute(
                                'data-dy-filter') == 'Производители':
                            brand_box = box
                            break
                    except:
                        continue
                for button in brand_box.find_elements(By.TAG_NAME, 'div'):
                    if button.get_attribute('role') == 'button':
                        button.click()
                        time.sleep(1)
                manufacturers = list(map(lambda x: x.text, brand_box.find_elements(By.TAG_NAME, 'a')))

            for i in range(10):
                driver.execute_script("window.scrollBy(0,1000)", "")
                time.sleep(1)

            if total_pages_count == -1:
                for button in driver.find_elements(By.TAG_NAME, 'a'):
                    try:
                        if button.get_attribute('role') == 'button' and '?page=' in button.get_attribute('href'):
                            total_pages_count = max(total_pages_count, int(button.get_attribute('href').split('?page=')[-1]))
                    except:
                        continue

            total_products_count = parse_html(driver.page_source, "eldorado.ru", category_name, total_products_count,
                                              manufacturers)

            if page_number + 1 <= total_pages_count * TESTING:
                page_number += 1
                driver.get(url + "/?page=" + str(page_number))
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
    boxes_1 = soup.find_all('li', class_='sl-hl-checked')
    for item in boxes_1:
        name=''
        link=''
        price=0
        try:
            for name_a in item.find_all('a'):
                try:
                    if name_a['data-dy'] == 'title':
                        link = name_a['href']
                        name = name_a.text
                        break
                except:
                    continue
            for price_span in item.find_all('span'):
                try:
                    if price_span['data-pc'] == 'offer_price':
                        price = price_span.text
                except:
                    continue

            pictures = list(map(lambda x: x.get('src'), item.find_all('img')))
            characteristics = ''
            characteristics_div = item.find_all('div', class_='eB')
            for div_c in characteristics_div:
                try:
                    to_add = ''
                    if characteristics != '':
                        to_add += ', '
                    to_add += div_c.find('span', class_='gB').text.strip() + ': ' + div_c.find('span', class_='hB').text.strip()
                except:
                    continue
                characteristics += to_add
        except:
            continue
        # insert into the database
        product_info = {'name': name.strip(),
                        'url': 'https://www.eldorado.ru' + link.strip(),
                        'cost': int(parse_price(price)),
                        'category': category_name,
                        'pictures': pictures,
                        'shop': 'Эльдорадо',
                        'manufacturer': determine_manufacturer(name, manufacturers),
                        'characteristics': characteristics,
                        }
        if total_products_count != 0:
            print(",", end="")
        total_products_count += 1
        # print(product_info)
        print(json.dumps(product_info))
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
    # get_data('https://www.eldorado.ru/c/kovriki-dlya-myshi', 'kovriki-dlya-myshi')
    arguments = sys.argv[1:]
    get_data(arguments[0], arguments[1])


if __name__ == "__main__":
    main()
