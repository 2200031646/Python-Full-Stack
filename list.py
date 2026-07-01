Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#list[]
a=[2,5.6,"pyhton",6+9j,True,False]
print(a)
[2, 5.6, 'pyhton', (6+9j), True, False]
type(a)
<class 'list'>
b=8
type(b)
<class 'int'>
c=[9]
type(c)
<class 'list'>
d=["pyhton","c","java","c++"]
d.append("DSA")
d
['pyhton', 'c', 'java', 'c++', 'DSA']
d.append("ml","dl")
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    d.append("ml","dl")
TypeError: list.append() takes exactly one argument (2 given)
d.append(["ml","dl"])
d
['pyhton', 'c', 'java', 'c++', 'DSA', ['ml', 'dl']]
#extend()
e=["ml","ai","ds"]
e.extend(["c","c++","python"])
e
['ml', 'ai', 'ds', 'c', 'c++', 'python']
#insert()
f=["vja","hyd"]
f.insert(1,"vzg")
f
['vja', 'vzg', 'hyd']
g=["pink","black","blue","orange"]
g.index("black")
1
g.copy()
['pink', 'black', 'blue', 'orange']
h=g.copy()
h
['pink', 'black', 'blue', 'orange']
h.count("pink")
1
#sort()
a=["grapes","apple","mango","banana"]
a.sort()
a
['apple', 'banana', 'grapes', 'mango']
>>> b=[8,6,0,3,6,1,2,20]
>>> b.sort()
>>> b
[0, 1, 2, 3, 6, 6, 8, 20]
>>> #reverse()
>>> a=[7,8,9,10,12,49,60]
>>> a.reverse()
>>> a
[60, 49, 12, 10, 9, 8, 7]
>>> b=["html","css","java"]
>>> b.reverse()
>>> b
['java', 'css', 'html']
>>> #pop()
>>> x=["c","c++","ml","dl"]
>>> x.pop()
'dl'
>>> x
['c', 'c++', 'ml']
>>> x.pop("c++")
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    x.pop("c++")
TypeError: 'str' object cannot be interpreted as an integer
>>> x.pop(1)
'c++'
>>> x
['c', 'ml']
>>> #remove()
>>> x.remove("ml")
>>> x
['c']
>>> #length
>>> a=["pooja","swathi","veni","sindhu"]
>>> len(a)
4
>>> b="sweety"
>>> len(b)
6
>>> c=["sweety"]
>>> len(c)
1
a.clear()
a
[]
b=[]
b.append("hi")
b
['hi']
