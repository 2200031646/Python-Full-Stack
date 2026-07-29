#math module
'''import math
print(math.pi)
print(math.pi*4)
print(math.sqrt(2))
print(math.log(2))
print(math.tan(45))
print(math.cos(60))
print(math.sin(30))
print(math.pow(2,4))
print(math.ceil(6.9))
print(math.floor(3.11))'''

#from keyword
'''from math import pi,sqrt,log,tan
print(pi)
print(sqrt(4))
print(log(6))
print(tan(45))'''

#sys module
'''import sys
print(sys.version)
print(sys.path)'''

#os module
'''import os
print(os.path)
print(os.getcwd())
print(os.listdir())
print(os.chdir("C:\\Users\\91955\\Downloads"))
print(os.listdir())'''

#random module
'''import random
a=random.sample(range(10,40),5)
print(a)'''

#randint()
'''import random
a=random.randint(50,60)
print(a)'''

#choice()
'''import random
a=[30,40,50,60,70]
b=random.choice(a)
print(b)'''

#task
'''import random
while True:
    input("Enter the roll of dice:")
    a=random.randint(1,6)
    print(a)
    b=input("roll again? (y/n):")
    if b == "y":
        continue
    elif b == "n":
        break
    else:
        print("Invalid option")'''
    
    
#calendar module
'''import calendar
year=2026
month=8
print(calendar.month(year,month))'''

#year
'''import calendar
year =2027
print(calendar.calendar(year))'''

'''import calendar
year=int(input("enter the year:"))
print(calendar.calendar(year))'''

'''import calendar
a=int(input("year:"))
b=int(input("month:"))
print(calendar.month(a,b))'''

#date & time
'''from datetime import date
a=date.today()
print(a)'''

'''import datetime
a=datetime.datetime.now()
print(a)'''

'''import time
a=time.time()
print(a) #epoch time

b=time.localtime(a)
print(b)

print(f"Today date is {b.tm_mday}-{b.tm_mon}-{b.tm_year}")
print(f"Today time is {b.tm_hour}:{b.tm_min}:{b.tm_sec}")
print(f"Today day is {b.tm_mday}-{b.tm_yday}-{b.tm_isdst}")'''

#Random Number Task
'''import random
import time
for i in range(10):
    a=random.randint(0,10)
    time.sleep(2)
    print(a)'''

#error handling
#syntax error -> compile error
#run_time error -> during execution time it will happen
#logical error ->error in logic(it can't be visible)

#Syntax error
'''for i in range(10)
print(i)'''

#Run_time Error
'''a=int(input())
b=int(input())
print(a//b)'''#10/0->zero division error

#Logical Error 
'''a=10
b=20
print(a-b)'''

#correct logic
'''a=10
b=20
if a<b:
    print("less")'''
#incorrect logic
'''a=10
b=20
if a>b:
    print("less")'''
# Exception Handling
#try->Instructions from which we are expecting the exceptions
#except->exceptions are raised in try block it will be handle by this block
#else->optional(no exceptions)
#finally->always it will display
'''while True:
    try:
        a=int(input("a value:"))
        b=int(input("b value:"))
        c=a//b
        print(c)
    except:
        print("exception is raised")
    else:
        print("no exceptions")
    finally:
        print("program ends....")'''
#regex(regular expressions)
'''a="codegnan is in vijayawada"
print(a)'''

'''a="codegnan\nis\tin\nvijayawada"
print(a)'''       

# Raw String (r"")
'''a=r"codegnan\nis\tin\nvij"
print(a)'''
#compile(),search(),findall(),split(),sub()

#sequence characters
#\w->it matches alphanumeric
#\W->it matches non-alpha numeric
#\d->it matches any digit
#\D->it matches non-digit
#\s->it represents white spaces
#\S->it represents non-white spaces

# compile()
'''import re
a = "mat cat maths money cash code cup dog donkey mug"
b = re.compile(r"m\w\w\w\w")
print(b)'''
# search()
'''c = b.search(a)
print(c)'''

'''b = re.search(r"m\w+", a)
print(b)'''
# findall()
'''c = re.findall(r"c\w+",a)
print(*c)'''
#split()
'''d=re.split(r"m",a)
print(d)

e=re.split(r"\S",a)
print(e)

#sub()
f=re.sub("m","a",a)
print(f)'''
# Regex Task
'''import re
a="year 2026 month 7 date 29"
b=re.findall(r"\d+",a)
print(b)
c=re.findall(r"\D+",a)
print(c)'''

'''import re
e="code dog donkey"'''
# Matching Words Containing 'd'
'''f=re.findall(r"d\w+",e)
print(f)'''
# Matching Words Starting with 'do' Using Word Boundary
'''g=re.findall(r"\bdo\w+",e)
print(g)'''
























