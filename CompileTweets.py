import os
import json

path = 'E:\\Poems'
finalpath = 'E:\\FinalData\\Tweet'
All_files = []
Listofdata = []
KeyId = 1;
for root, dirs, files in os.walk(path):
    for filename in files:
        All_files.append(root + '\\' + filename)
path = All_files[0]
for path in All_files:
    with open(path, 'r') as fp:
        data = json.loads(fp.read())
        appDict = {'id': 0,
                   'title': '',
                   'author': '',
                   'lines': '',
                   'Total chara': 0
                   }

        for poem in data:
            appDict['id'] = KeyId
            KeyId += 1
            appDict['title'] = poem['title']
            appDict['author'] = poem['author']
            appDict['lines'] = str(poem['lines'][0:5])
            temp = len(poem['title']) + len(poem['author']) + len(str(poem['lines'][0:4]))
            appDict['Total chara'] = len(poem['title']) + len(poem['author']) + len(str(poem['lines'][0:4]))
            if temp <= 260:
                Listofdata.append(appDict.copy())
            appDict.clear()
with open(finalpath, 'w') as f:
    json.dump(Listofdata, f,indent=2)
