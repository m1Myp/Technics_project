import json

# Чтение из JSON файлов
# С последующим сравнением штук.
# Добро пожаловать на сервер шизофрения
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

engNotNeedWord = ["usb"]

for input_txt in txtBase:
    with open(input_txt, encoding='utf-8', mode="r") as json_file:
        data = json.loads(json_file.read())
        print(data)
        for p in data:
            name = p["name"].lower()
            newTempStuff = name.split() #Темпик для создания токенов с помощью сплита, чтобы не каверкать изначальный нейм продукта
            anotherTempStuff = ["", "", "", ""] #Хранитель актуальных токенов в системе
            # fuzz.token_sort_ratio еще кринжовее?
            for tempName in newTempStuff:
                subname = ''.join(ch for ch in tempName if ch.isalnum()) #Создание токена без мусора только символы и цифры
                breakFlag = False
                for color in colors.values():
                    if subname in color:
                        anotherTempStuff[2] = color[0]
                        breakFlag = True
                        break
                if breakFlag:
                    continue
                for characteristic in characteristics.values():
                    if subname == characteristic:
                        anotherTempStuff[1] = subname
                        breakFlag = True
                        break
                if breakFlag:
                    continue
                if any(map(str.isdigit, subname)):
                    anotherTempStuff[3] += subname
                    breakFlag = True
                    break
                if breakFlag:
                    continue
                if re.search(r'[a-z0-9]', subname):
                    if(subname in engNotNeedWord):
                        continue
                    anotherTempStuff[0] += subname
            finalName = ""
            #Сюда надо добавить сохранение в буфер anotherTempStuff перед его записью для сравнения
            for i in range(len(anotherTempStuff)): #Вот эта штука, кстати не обязательно в нашем случае
                finalName += anotherTempStuff[i]   #, ибо сравниваем не неймы а токены
                #Реализовать метод замены эмптиблоков на "подходящии" только как....
            #Просто сравнивать с помощью fuzz.ratio свучит кринжово... и не выгодно
            #Вот здесь токены должны сравниваться с токенами которые я запишу ранее в отдельный файлик
            #Токены проверяются по порядку
            #Разное имя -> новый товар ИНАЧЕ
            #Разный "номер товара" -> новый товар ИНАЧЕ
            #Разный цвет -> новый товар ИНАЧЕ
            #Цвет пуст -> Что-то делаем чтобы сравнить с токенами которые уже существуют
            #Мои 2 варианта - превращать пустой токен во все токены которые позволяет словарь цветов, ИЛИ
            #Сделать токены пустыми в тех вещах которые мы сравниваем с этим товаром
            #Проблема и того и того метода, что он работает до первого вхождения, что не есть good
            #Если цвет не пуст и совпадает идем дальше
            #Смотри пункт про цвета, только это пункт про "характеристики" а.ля беспроводная
            if (finalName in dataBase) or (anotherTempStuff[3] in codeDataBase):
                oldLinks = dataBase.pop(finalName)
                oldLinks.append(p['link'])
                dataBase[finalName] = oldLinks
            else:
                dataBase[finalName] = [p['link']]
                codeDataBase[finalName] = anotherTempStuff[3]
print(dataBase)


