Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#operators
#arthematic operators
a=4
b=8
print(a+b)
12
print(a-b)
-4
print(a*b)
32
print(a//b)
0
print(a/b)
0.5
print(a**b)
65536
print(a%b)
4
#assignment operators
c=5
d=10
print(c+=d)
SyntaxError: invalid syntax
c+=d
c
15
print(c)
15
c-=4
c
11
c*=3
c
33
c//=2
c
16
c/=4
c
4.0
c**=3
c
64.0
c%=6
c
4.0
#comparision operators
x=6
y=12
x<y
True
x>y
False
y>x
True
y<x
False
x>=y
False
x<=y
True
x!=y
True
x==y
False
y>=x
True
y<=x
False
#logical operators
p=8
q=4
p<q and q>p
False
p>q and q<p
True
p>=q and q<=p
True
p<q or q<p
True
>>> p!=q or q==p
True
>>> p!=q and p==q
False
>>> not True
False
>>> not False
True
>>> #identity operators
>>> z=8
>>> type(z) is int
True
>>> type(z) is not int
False
>>> t=6.7
>>> type(t) is float
True
>>> type(t) is str
False
>>> #membership operators
>>> m = 2,3,4,5,6,7,8,9
>>> 4 in m
True
>>> 89 in m
False
>>> 78 not in m
True
>>> #identity operators
>>> f="hi"
>>> type(f) is str
True
>>> type(f) is not int
True
>>> type(f) is not str
False
>>> g=4+9j
>>> type(g) is complex
True
>>> type(g) is str
False
>>> r = True
>>> type(r) is bool
True
>>> type(r) is complex
False
