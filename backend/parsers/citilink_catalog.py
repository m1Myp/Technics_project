import json
import sys
import time

import requests
import undetected_chromedriver
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

TESTING = 1


def solve_captcha(driver):
    while len(driver.find_elements(By.ID, 'captcha_image')) != 0:
        image = driver.find_element(By.ID, 'captcha_image').get_attribute('src').replace('data:image/png;base64, ',
                                                                                         '').strip()
        result = read_image(image)
        form = driver.find_element(By.TAG_NAME, 'form')
        label = form.find_element(By.TAG_NAME, 'label')
        label.send_keys(result)
        button = form.find_element(By.TAG_NAME, 'button')
        button.click()
        time.sleep(3)


def read_image(image):
    r = requests.post("http://rucaptcha.com/in.php",
                      data={'key': 'b2ba6a674fdf3f0f80355bd43165eefd', 'method': 'base64',
                            'body': image, 'json': 1})
    response = json.loads(r.content.decode('utf-8'))
    if response['status'] != 1:
        print("BAD captcha request")
    else:
        req_id = response['request']
        # print(req_id)
        time.sleep(5)
        while True:
            r = requests.post("http://rucaptcha.com/res.php",
                              data={'key': 'b2ba6a674fdf3f0f80355bd43165eefd', 'action': 'get',
                                    'id': int(req_id), 'json': 1})
            response = json.loads(r.content.decode('utf-8'))
            if response['status'] == 1:
                # print("result:", response['request'])
                return response['request']


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
    print("[")
    try:
        driver.get(url + "/?view_type=grid")
        # for the while loop
        flag = True
        page_number = 1
        total_pages_count = -1
        manufacturers = []
        while flag:
            time.sleep(2)
            solve_captcha(driver)
            for i in range(5):
                driver.execute_script("window.scrollBy(0,1200)", "")
                time.sleep(1)
            driver.execute_script("window.scrollBy(0,-500);")
            time.sleep(2)

            if total_pages_count == -1:
                total_pages_count = int(driver.find_elements(By.CLASS_NAME, "app-catalog-h5nagc")[-1].text)
            if len(manufacturers) == 0:
                brand_box = -1
                for box in driver.find_elements(By.CLASS_NAME, 'app-catalog-1gdmf2q'):
                    if box.get_attribute('data-meta-value') == 'Бренд':
                        brand_box = box
                        break
                button = brand_box.find_element(By.CLASS_NAME, 'app-catalog-u45ylu')
                driver.execute_script("arguments[0].click();", button)
                time.sleep(1)
                manufacturers = list(
                    map(lambda x: x.text, brand_box.find_elements(By.CLASS_NAME, 'app-catalog-1sylyko')))

            total_products_count = parse_html(driver.page_source, "citilink.ru", category_name, total_products_count,
                                              manufacturers)

            if page_number + 1 <= total_pages_count * TESTING:
                page_number += 1
                driver.get(url + "/?view_type=grid&p=" + str(page_number))
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
    laptop_boxes = soup.find_all('div', class_='e1ex4k9s0 app-catalog-1bogmvw e1loosed0')
    for laptop in laptop_boxes:
        try:
            name = laptop.find('div', class_='app-catalog-oacxam e1xes8vl0').a.get('title')
            link = url + laptop.find('div', class_='app-catalog-oacxam e1xes8vl0').a.get('href')
            price = laptop.find('span', class_='e1j9birj0 e106ikdt0 app-catalog-175fskm e1gjr6xo0').text
            pictures = list(
                map(lambda x: x.get('src'), laptop.find('div', class_='app-catalog-lxji0k e153n9o30').find_all('img')))
            product_info = {'name': name.strip(),
                            'url': 'https://www.' + link.strip(),
                            'cost': int(price.replace(" ", "")),
                            'category': category_name,
                            'pictures': pictures,
                            'shop': 'Ситилинк',
                            'manufacturer': determine_manufacturer(name, manufacturers),
                            }
            if total_products_count != 0:
                print(",", end="")
            total_products_count += 1
            print(json.dumps(product_info))
        except:
            continue
    return total_products_count


def determine_manufacturer(name, manufacturers):
    for manufacturer in manufacturers:
        if manufacturer.lower() in name.lower():
            return manufacturer
    return ''


def main():
    # get_data('https://www.citilink.ru/catalog/myshi', 'myshi')
    arguments = sys.argv[1:]
    get_data(arguments[0], arguments[1])


if __name__ == "__main__":
    main()
