Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#multiple variable assignment
a=4,b=9
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
a=4;b=9
print(a+b)
13
a,b=2,3
print(a+b)
5
#assigning same value to multiple variables
a,b,c=10
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    a,b,c=10
TypeError: cannot unpack non-iterable int object
a=b=c=10
print(a,b,c)
10 10 10
#assigning different values to multiple variables
a,b,c=2,3,4
print(a,b,c)
2 3 4
a,b,c=2,3,4,5,6,7,8
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    a,b,c=2,3,4,5,6,7,8
ValueError: too many values to unpack (expected 3, got 7)
>>> #tuple unpacking
>>> x,y,z=(3,4,5)
>>> print(x,y,z)
3 4 5
>>> #variable name without spaces
>>> first name="yasaswini"
SyntaxError: invalid syntax
>>> first_name="yasaswini"
>>> print(first_name)
yasaswini
>>> firstname="yasaswini"
>>> print(firstname)
yasaswini
>>> #string concatenation
>>> fname="yasaswini"
>>> lname="abburi"
>>> print(fname+lname)
yasaswiniabburi
>>> print(fname+" "+lname)
yasaswini abburi
>>> print(fname,lname)
yasaswini abburi
>>> case-sensitive variable names
SyntaxError: invalid syntax
>>> #case-sensitive variable names
>>> name="yasaswini"
>>> print(name)
yasaswini
>>> NAME="yasaswini"
>>> print(NAME)
yasaswini
>>> Name="yasaswini"
>>> print(Name)
yasaswini
>>> #deleting variables
>>> d=5
>>> print(d)
5
>>> del d
>>> print(d)
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    print(d)
NameError: name 'd' is not defined. Did you mean: 'id'?
