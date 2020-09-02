import requests
import json

#Create Poem dataset
url = 'http://poetrydb.org/author'
resp = requests.get(url).json()
authors = resp['authors']

for author in authors:
    new_url = url + '/' + author
    response = requests.get(new_url).json()
    path = 'E:\Poems' + '\\' + author
    with open(path, 'w') as fp:
        json.dump(response, fp, indent=6)


