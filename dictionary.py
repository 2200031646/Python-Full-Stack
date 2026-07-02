Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#dict()
a={"name":"yasaswini","city":"via"}
print(a)
{'name': 'yasaswini', 'city': 'via'}
type(a)
<class 'dict'>
b={3,4,5,6,7,"sweety"}
type(b)
<class 'set'>
a={"name":"yasaswini","mailid":"yasaswini.abburi@gmail.com","mobileno":"9875634527"}
print(a)
{'name': 'yasaswini', 'mailid': 'yasaswini.abburi@gmail.com', 'mobileno': '9875634527'}
a.keys()
dict_keys(['name', 'mailid', 'mobileno'])
a.values()
dict_values(['yasaswini', 'yasaswini.abburi@gmail.com', '9875634527'])
a.items()
dict_items([('name', 'yasaswini'), ('mailid', 'yasaswini.abburi@gmail.com'), ('mobileno', '9875634527')])
c={"course":"python","institute":"codegnan","name":"yasaswini"}
c.update({"place":"vijayawada"})
c
{'course': 'python', 'institute': 'codegnan', 'name': 'yasaswini', 'place': 'vijayawada'}

c.update({"year":2026},{"month":7})
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    c.update({"year":2026},{"month":7})
TypeError: update expected at most 1 argument, got 2
c.update({"year":2026,"month":7})
c
{'course': 'python', 'institute': 'codegnan', 'name': 'yasaswini', 'place': 'vijayawada', 'year': 2026, 'month': 7}
a={"year":2026,"month":"july"}
a.setdefault("date",2)
2
a
{'year': 2026, 'month': 'july', 'date': 2}
a={"time":12,"hour":1,"min":3}
a.pop()
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    a.pop()
TypeError: pop expected at least 1 argument, got 0
a.pop("time")
12
a
{'hour': 1, 'min': 3}
a.popitem()
('min', 3)
a
{'hour': 1}
a={"college":"klu","branch":"cse"}
a.get("college")
'klu'
a["branch"]
'cse'
a
{'college': 'klu', 'branch': 'cse'}
>>> a["cse"]
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    a["cse"]
KeyError: 'cse'
>>> d={"hour":12,"min":3,"sec":60}
>>> d.copy()
{'hour': 12, 'min': 3, 'sec': 60}
>>> d
{'hour': 12, 'min': 3, 'sec': 60}
>>> d.clear()
>>> d
{}
>>> e={}
>>> e.update({"name":"yashu"})
>>> e
{'name': 'yashu'}
>>> a={"name":"yasaswini","course":"python","year":2026}
>>> len(a)
3
>>> a.count("name")
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    a.count("name")
AttributeError: 'dict' object has no attribute 'count'
>>> x={"name":"yasaswini","city":"via","name":"yasaswini"}
>>> print(x)
{'name': 'yasaswini', 'city': 'via'}
>>> x={"name":"yasaswini","city":"via","name":"priya"}
>>> print(x)
{'name': 'priya', 'city': 'via'}
>>> x={"name1":"yasaswini","city":"via","name2":"yasaswini"}
>>> print(x)
{'name1': 'yasaswini', 'city': 'via', 'name2': 'yasaswini'}
>>> a={"idnos":[10,20,30],"name":["suni","vijitha","srujana"],"marks":[60,70,80]}
>>> print(a)
{'idnos': [10, 20, 30], 'name': ['suni', 'vijitha', 'srujana'], 'marks': [60, 70, 80]}
>>> type(a)
<class 'dict'>
>>> a.keys()
dict_keys(['idnos', 'name', 'marks'])
>>> a.values()
dict_values([[10, 20, 30], ['suni', 'vijitha', 'srujana'], [60, 70, 80]])
>>> a.items()
dict_items([('idnos', [10, 20, 30]), ('name', ['suni', 'vijitha', 'srujana']), ('marks', [60, 70, 80])])
