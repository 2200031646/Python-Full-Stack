Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #variables
>>> print(3+3)
6
>>> #storing and printing values
>>> a=10
>>> b=2
>>> c=4
>>> print(b+c)
6
>>> #case-senstivity in python
>>> x=20
>>> print(X)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    print(X)
NameError: name 'X' is not defined. Did you mean: 'x'?
>>> print(x)
20
>>> y=30
>>> print(y)
30
>>> Z=40
>>> print(Z)
40
>>> #variable naming rules
>>> 3=50
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
>>> a3=50
>>> print(a3)
50
>>> 4a=90
SyntaxError: invalid decimal literal
>>> a0123456789=100
>>> print(a0123456789)
100
>>> #string variables
>>> name="yasaswini"
>>> print(name)
yasaswini
>>> print("name")
name
>>> city="vja"
>>> print(city)
vja
>>> country="india"
print(country)
india
#using underscore in variables
@a=40
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
_=20
print(_)
20
_b=100
print(_b)
100
#email as a string variable
mailid="yasaswini.abburi@gmail.com"
print(mailid)
yasaswini.abburi@gmail.com
#reserved keywords cannot be used as variables
if=30
SyntaxError: invalid syntax
elif=50
SyntaxError: invalid syntax
print=19
print(print)
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    print(print)
TypeError: 'int' object is not callable
#multiple variable assignment
e=4,f=9
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
e=4;f=9
print(e+f)
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    print(e+f)
TypeError: 'int' object is not callable
