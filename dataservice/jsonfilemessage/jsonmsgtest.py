import  json



import json

jsonData = '{"a":{"x":1,"y":2},"b":2,"c":3,"d":4,"e":5}';

text = json.loads(jsonData)
print(text)
print(text[0])  #这个将会报错