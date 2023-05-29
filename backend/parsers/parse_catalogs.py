import platform
import subprocess
import json

from products.tools.work_with_db import clean_db, load_many_products
from parsers.settings import mvideo_urls, citilink_urls


def parse_catalogs():
    # clean_db()
    data = []
    for category in mvideo_urls:
        for url in mvideo_urls[category]:
            if platform.system() == 'Windows':
                proc = subprocess.Popen(
                    "venv\Scripts\python.exe parsers\mvideo_catalog.py " + url + " " + category,
                    stdout=subprocess.PIPE)
            else:
                proc = subprocess.Popen(
                    "venv/Scripts/python parsers/mvideo_catalog.py " + url + " " + category,
                    stdout=subprocess.PIPE)
            load_many_products(data)
            data = json.load(proc.stdout)
            # print(data)

    for category in citilink_urls:
        for url in citilink_urls[category]:
            if platform.system() == 'Windows':
                proc = subprocess.Popen(
                    "venv\Scripts\python.exe parsers\citilink_catalog.py " + url + " " + category,
                    stdout=subprocess.PIPE)
            else:
                proc = subprocess.Popen(
                    "venv/Scripts/python parsers/citilink_catalog.py " + url + " " + category,
                    stdout=subprocess.PIPE)
            load_many_products(data)
            data = json.load(proc.stdout)
            # print(data)

    load_many_products(data)