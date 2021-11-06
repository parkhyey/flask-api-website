import requests
import json

wiki = 'Russian_Blue'
data = requests.get(''+wiki)
print(data.text)
print(type(data.text))

json_obj=json.loads(data.text)
print(json_obj)