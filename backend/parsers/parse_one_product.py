import platform

import subprocess
import json

from products.tools.work_with_db import update_product_cost

TESTING = False


def parse_one_product(url):
    if TESTING:
        if url.startswith('https://www.mvideo.ru'):
            avail = [{'shop_name': 'ТЦ «МЕГА Новосибирск»',
                      'shop_place': 'Новосибирск, ул. Ватутина, д. 107, ТЦ «МЕГА Новосибирск»',
                      'date': 'через 15 минут'},
                     {'shop_name': 'ТПС «Галерея Новосибирск»',
                      'shop_place': 'Новосибирск, ул. Гоголя, д. 13, ТПС «Галерея Новосибирск»',
                      'date': '1 июня'}]
            update_product_cost({'url': url, 'cost': 1234})
            return {'cost': 1234, 'availability': avail}
        if url.startswith('https://www.citilink.ru'):
            avail = [{'shop_name': 'Магазин Новосибирск, ТЦ "Юпитер"',
                      'shop_place': 'Новосибирск, ул Гоголя, д.15, ТЦ Юпитер, 1 этаж',
                      'date': 'Завтра'},
                     {'shop_name': 'Пункт выдачи Ситилинк Новосибирск, ТЦ "Академгородка"',
                      'shop_place': 'Новосибирск, ул Ильича, д.6, ТЦ Академгородка, 2 этаж',
                      'date': '31 мая'}]
            update_product_cost({'url': url, 'cost': 1234})
            return {'cost': 4312, 'availability': avail}
    if url.startswith('https://www.eldorado.ru'):
        avail = [{'shop_name': 'Sorry, we don\'t have parser yet for this site',
                  'shop_place': '',
                  'date': 'soon'},
                 ]
        return {'cost': -1, 'availability': avail}
    script_name = ''
    if url.startswith('https://www.mvideo.ru'):
        script_name = 'mvideo_one_product.py'
    if url.startswith('https://www.citilink.ru'):
        script_name = 'citilink_one_product.py'
    if platform.system() == 'Windows':
        proc = subprocess.Popen(
            "venv\Scripts\python.exe parsers\\" + script_name + ' ' + url, stdout=subprocess.PIPE)
    else:
        proc = subprocess.Popen(
            "venv/Scripts/python parsers/" + script_name + ' ' + url, stdout=subprocess.PIPE)
    data = json.load(proc.stdout)
    cost = data['cost']
    update_product_cost({'url': url, 'cost': cost})
    return data
