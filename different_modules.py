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
    































