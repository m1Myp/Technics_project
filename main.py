import json
import numpy
# Чтение из JSON файлов
# С последующим сравнением штук.
# Добро пожаловать на сервер шизофрения
from pprint import pprint
import re
from string import ascii_letters as en
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

dataBase = {}
codeDataBase = {}
txtBase = ["things.json", "things1.json", "things2.json"]

colors = {"yellow": ["yellow", "желтый", "жёлтый", "желтая", "жёлтая"], "orange": ["orange", "оранжевый", "оранжевая"],
          "red": ["red", "красный", "красная"], "violet": ["violet", "фиолетовый", "фиолетовая"],
          "blue": ["blue", "синий", "синяя"], "green": ["green", "зеленый", "зеленая"],
          "grey": ["grey", "серый", "серая"], "brown": ["brown", "коричневый", "коричневая"],
          "gold": ["gold", "золотой", "золотая"], "black": ["black", "черный", "черная"],
          "white": ["white", "белый", "белая"]}

characteristics = {"wireless": ["wireless", "беспроводной", "беспроводная"]}

engNotNeedWord = ["usb", "провдная", "проводной"]

for input_txt in txtBase:
    with open(input_txt, encoding='utf-8', mode="r") as json_file:
        data = json.loads(json_file.read())
        print(data)
        for p in data:
            name = p["name"].lower()
            newTempStuff = re.sub("\[.*?\]","", name)
            newTempStuff = newTempStuff.split()  # Темпик для создания токенов с помощью сплита, чтобы не каверкать изначальный нейм продукта
            # Сплит производится по пробелу
            anotherTempStuff = ["", "", "", ""]  # Хранитель актуальных токенов в системе
            # fuzz.token_sort_ratio еще кринжовее?
            for tempName in newTempStuff:
                subname = ''.join(
                    ch for ch in tempName if ch.isalnum())  # Создание токена без мусора только символы и цифры
                breakFlag = False
                for color in colors.values():  # Проход по словарю цветов, если есть совпадение добавляем в буфер токена на позицию 2
                    if subname in color:
                        anotherTempStuff[2] = color[0]
                        breakFlag = True
                        break
                if breakFlag:
                    continue
                for characteristic in characteristics.values():  # Проход по словарю характеристик, если есть совпадение добавляем в буфер токена на позицию 3
                    if subname == characteristic:
                        anotherTempStuff[3] = subname
                        breakFlag = True
                        break
                if breakFlag:
                    continue
                if any(map(str.isdigit,
                           subname)):  # Если в токене есть хотя бы 1 символ он пишется в буфер токена на позицию 1
                    # Нужно реализовать проверку на наличие в слове скобочек, для игнорирования рандомного кода товара внутри названия
                    anotherTempStuff[1] += subname
                    breakFlag = True
                if breakFlag:
                    continue
                if re.search(r'[a-z0-9]', subname):  # Если в токене английские буквы, то это название товара
                    if (subname in engNotNeedWord):  # Проверка что это не английское слово которое нам не нужно, типо USB/HDMI/...
                        continue
                    anotherTempStuff[0] += subname
            id = 0
            finalName = ""
            newBuferIwannaToImportToJSONLater = []
            for i in range(0, len(newBuferIwannaToImportToJSONLater)+2):
                if i == 0:
                    newBuferIwannaToImportToJSONLater.append(anotherTempStuff)
                    continue
                if(fuzz.ratio(anotherTempStuff[0], newBuferIwannaToImportToJSONLater[i-1][0]) > 75):
                    finalName = anotherTempStuff[0]
                else:
                    finalName = newBuferIwannaToImportToJSONLater[i-1][0]
                if (finalName+anotherTempStuff[1]+anotherTempStuff[2]+anotherTempStuff[3] in dataBase) \
                        and (anotherTempStuff[3] in newBuferIwannaToImportToJSONLater[i-1][3]
                             or (anotherTempStuff[3] == "")) \
                        and (anotherTempStuff[2] in newBuferIwannaToImportToJSONLater[i-1][2]
                             or (anotherTempStuff[2] == "")) \
                        and (anotherTempStuff[1] in newBuferIwannaToImportToJSONLater[i-1][1]
                             or anotherTempStuff[1] == ""):
                    oldLinks = dataBase.pop(finalName+anotherTempStuff[1]+anotherTempStuff[2]+anotherTempStuff[3])
                    oldLinks.append(p['link'])
                    dataBase[finalName+anotherTempStuff[1]+anotherTempStuff[2]+anotherTempStuff[3]] = oldLinks
                    newBuferIwannaToImportToJSONLater[id] = anotherTempStuff
                    id += 1
                else:
                    dataBase[finalName+anotherTempStuff[1]+anotherTempStuff[2]+anotherTempStuff[3]] = [p['link']]
                    newBuferIwannaToImportToJSONLater.append(anotherTempStuff)
pprint(dataBase)

# Сюда надо добавить сохранение в буфер anotherTempStuff перед его записью для сравнения
# Вот здесь токены должны сравниваться с токенами которые я запишу ранее в отдельный файлик
# Токены проверяются по порядку
# Разное имя -> новый товар ИНАЧЕ
# Разный "номер товара" -> новый товар ИНАЧЕ
# Разный цвет -> новый товар ИНАЧЕ
# Цвет пуст -> Что-то делаем чтобы сравнить с токенами которые уже существуют
# Мои 2 варианта - превращать пустой токен во все токены которые позволяет словарь цветов, ИЛИ
# Сделать токены пустыми в тех вещах которые мы сравниваем с этим товаром
# Проблема и того и того метода, что он работает до первого вхождения, что не есть good
# Если цвет не пуст и совпадает идем дальше
# Смотри пункт про цвета, только это пункт про "характеристики" а.ля беспроводная
