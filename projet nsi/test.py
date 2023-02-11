import json

#projet nsi\test.json

js = open(r"projet nsi\test.json")

text = json.load(js)

print(text)