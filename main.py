import json

# Чтение из JSON файлов

dataBase = {}
txtBase = ["things.json", "things1.json"]

for input_txt in txtBase:
    with open(input_txt, "r") as json_file:
        data = json.loads(json_file.read())
        print(data)
        for p in data:
            if not (p['name'] in dataBase):
                dataBase[p['name']] = [p['link']]
            else:
                oldLinks = dataBase.pop(p['name'])
                linksBase = [p['link'], oldLinks]
                dataBase[p['name']] = linksBase

print(dataBase)

