import json

with open('data.json', 'r', encoding='utf-8') as f:
    s = json.load(f)

dict1 = {}


def dic(d):
    for key, value in d.items():
        if type(value) == int:
            dict1.update({key: value})


def func(s):
    for key, value in s.items():
        if type(value) == int:
            dict1.update({key: value})
        elif type(value) == list:
            for element in value:
                if type(element) == dict:
                    dic(element)
        elif type(value) == dict:
            dic(value)


func(s)
p2_dict = sorted(dict1.items(), key=lambda d: d[1],reverse=True)
with open('p2.txt','w',encoding='utf-8') as f:
    json.dump(p2_dict,f)