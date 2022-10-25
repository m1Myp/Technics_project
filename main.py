import json

# Чтение из JSON файла

dataBase = {}

with open('things.json') as json_file, open('things1.json') as json_file2:
    data = json.load(json_file)
    data1 = {}
#    data1 = json.load(json_file2)
    print(data)
    for p in data:
        dataBase[p['name']] = [p['link']]

#    for p in data1:
#        if not (p['name'] in dataBase):
#            dataBase[p['name']] = [p['link']]
#        else:
#            oldLinks = dataBase.pop(p['name'])
#            linksBase = [p['link'], oldLinks]

print(dataBase)

#        print('Name: ' + p['name'])
#        print('Price: ' + p['price'])
#        print('Website: ' + p['link'])
#        print('')


