import json

# Чтение из JSON файлов

dataBase = {}
txtBase = ["things.json", "things1.json", "things2.json"]

for input_txt in txtBase:
    with open(input_txt, "r") as json_file:
        data = json.loads(json_file.read())
        print(data)
        for p in data:
            lowerName = p['name'].lower()
            name = "".join(c for c in lowerName if c.isalnum())
            if not (name in dataBase):
                dataBase[name] = [p['link']]
            else:
                oldLinks = dataBase.pop(name)
                oldLinks.append(p['link'])
                dataBase[name] = oldLinks

print(dataBase)



