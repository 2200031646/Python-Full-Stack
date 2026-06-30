Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#String methods
#len()
a="python"
len(a)
6
b="python course"
len(b)
13
c=""
len(c)
0
d=" "
len(d)
1
#count
a="twinkle twinkle little star"
count(a)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    count(a)
NameError: name 'count' is not defined. Did you mean: 'round'?
a.count("twinkle")
2
a.count("t")
5
a.count("k")
2
a.count(" ")
3
#find a string
a="code"
a[1]
'o'
a.find("d")
2
a.find("e")
3
b="happy"
b.find("p")
2
b[2:4]
'pp'
#escape sequence
#\n->new line
#\t->tab space
a="name\nmobile\tmailid\nclg"
print(a)
name
mobile	mailid
clg
b="Name:Yasaswini\nMobileno:9876543210\tMailid:yasaswini.abburi@gmail.com\nClg:Klu"
print(b)
Name:Yasaswini
Mobileno:9876543210	Mailid:yasaswini.abburi@gmail.com
Clg:Klu
#replace
a="wait until you succeed"
a.replace("wait","work")
'work until you succeed'
a
'wait until you succeed'
b="wait wait until you succeed")
SyntaxError: unmatched ')'
b="wait wait until you succeed"
b.replace("wait","work")
'work work until you succeed'
b.replace("wait","work",1)
'work wait until you succeed'
#upper()
c="hello"
c.upper()
'HELLO'
#lower()
d="INDIA"
d.lower()
'india'
e="python"
e.upper(0)
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    e.upper(0)
TypeError: str.upper() takes no arguments (1 given)
e[0].upper()
'P'
e.capitalize()
'Python'
f="full stack"
f.title()
'Full Stack'
g="i am in class"
g.title()
'I Am In Class'
a="java"
a.isupper()
False
a.islower()
True
a.isdigit()
False
a.isalpha()
True
b="exam hall"
b.isalpha()
False
c="examhall"
c.isalpha()
True
d="12345"
d.isdigit()
True
d=1234
d.isdigit()
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    d.isdigit()
AttributeError: 'int' object has no attribute 'isdigit'
e="1234"
e.isdigit()
True
e.isalnum()
True
f="yashu1234"
f.isalnum()
True
g="yashu@22"
g.isalnum()
False
x="hello pyhton"
x.startswith("h")
True
x.endswith("n")
True
#strip()
#lstrip(),rstrip()
y="          yasaswini         "
y.strip()
'yasaswini'
y.lstrip()
'yasaswini         '
y.rstrip()
'          yasaswini'
z="   how   are   you  "
z.strip()
'how   are   you'
#split()
p="python java c c++"
p.split()
['python', 'java', 'c', 'c++']
q="codegnan"
q.split()
['codegnan']
#join()
s="vja hyd vzg"
"".join(s)
'vja hyd vzg'
t="vja","hyd","vzg"
"".join(t)
'vjahydvzg'
" ".join(t)
'vja hyd vzg'
"k".join(t)
'vjakhydkvzg'
#concatenation
a="hello"
b="world"
print(a+b)
helloworld
print(a+" "+b)
hello world
fname="yasaswini"
lname="abburi"
print(fname+lname)
yasaswiniabburi
print(fname+" "+lname)
yasaswini abburi
print(fname.title()+" "+lname.title())
Yasaswini Abburi
print((fname+" "+lnmae).title())
Traceback (most recent call last):
  File "<pyshell#107>", line 1, in <module>
    print((fname+" "+lnmae).title())
NameError: name 'lnmae' is not defined. Did you mean: 'lname'?
>>> print((fname+" "+lname).title())
Yasaswini Abburi
>>> #formatting
>>> a=4
>>> b=8
>>> print(a+b)
12
>>> print("the sum is",a+b)
the sum is 12
>>> x="vja"
>>> print("city is",x)
city is vja
>>> #format method
>>> j="motu"
>>> k="patlu"
>>> print("hello",j+k)
hello motupatlu
>>> print("hello {}{}".format(j,k))
hello motupatlu
>>> print("hello {} {}".format(j,k))
hello motu patlu
>>> print("hello {} hello {}".format(j,k))
hello motu hello patlu
>>> #fstring
>>> l="sita"
>>> m="rama"
>>> print(f"hello {l}{m}")
hello sitarama
>>> print(f"hello {l} {m}")
hello sita rama
>>> print(f"hello {l} hello {m}")
hello sita hello rama
>>> a=5
>>> b=10
>>> c=a*b
>>> print(f"the product is {c}")
the product is 50
>>> print(f"the product is {a*b}")
the product is 50
>>> print("the product is {}".format(a*b))
the product is 50
>>> print("the product is {}".format(c))
the product is 50
