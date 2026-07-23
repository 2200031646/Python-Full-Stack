#built-in functions
#directory-collection of files

#print(dir())

#print(dir("__builtins__"))

#fromkeys()
'''a="codegnan"
print(a)
print(list(a))
print(tuple(a))

print(set(a))
#print(dict(a))
b=dict.fromkeys(a)
print(b)

c=dict.fromkeys(a,"yashu")
print(c)

c["d"]="python"
print(c)'''

#eval()
'''while True:
    a=int(input("a value:"))
    b=int(input("b value:"))
    print(a+b)'''

'''while True:
    a=float(input("a value:"))
    b=float(input("b value:"))
    print(a+b)'''

'''while True:
    a=input("a value:")
    b=input("b value:")
    print(a+b)'''

'''while True:
    a=eval(input("a value:"))
    b=eval(input("b value:"))
    print(a+b)'''

#zip()->we can combine multiple collections into one collection
'''a=[10,20,30,40,50,60]
names=["yashu","suni","sweety","vijitha","srujana"]
print(a+names)

#b=zip(a,name)
#print(b)

c=list(zip(a,names))
print(c)

c=tuple(zip(a,names))
print(c)

c=set(zip(a,names))
print(c)

c=dict(zip(a,names))
print(c)'''

#enumerate()->we can give counter to the collection
'''names=["tarani","siri","nikitha","prameela","kalyani"]
for i in range(len(names)):
    print(i,names[i])

b=list(enumerate(names))
print(b)

b=list(enumerate(names,10))
print(b)

b=dict(enumerate(names,100))
print(b)'''

#ASCII-American Standard Code for Information Interchange
#chr()
#ord()
'''print(chr(65))

print(chr(90))

print(chr(92))

print(ord("a"))

print(ord("z"))

print(ord("y"))

print(ord(89))'''

#task
'''for i in range(65,91):
    print(chr(i),end=" ")

for i in range(97,123):
    print(chr(i),end=" ")'''

'''n=input("Enter:")
for i in n:
    print(i,"-",ord(i))'''

#BMI
'''while True:
    w = float(input("Enter the weight(kg):"))
    h=float(input("Enter the height(m):"))
    bmi = w / (h * h)
    print("BMI =", bmi)
    if bmi <= 18.5:
        print("Under Weight")
    elif bmi > 18.5 and bmi <= 24.5:
        print("Healthy Weight")
    elif bmi > 24.5 and bmi <=29.5:
        print("Over Weight")
    elif bmi>30.5:
        print("Obesity")'''


#annonymous functions(nameless function)
#write a function to calculate 2*x+5 where x=5

'''def check():
    x=int(input("Enter value:"))
    print(2*x+5)
check()'''

'''def check(x):
    print(2*x+5)
check(5)'''

#syntax
#a=lambda arg:expr
'''a=lambda x:2*x+5
print(a(5))'''

'''a=int(input())
b=lambda x:2*x+5
print(b(a))'''

#tasks
'''a=lambda x,y:x*y
print(a(5,6))'''

'''x=int(input())
y=int(input())
z=lambda x,y:x*y
print(z(x,y))'''

#a=codegnan
#CODEGNAN
'''a=input()
b=lambda a:a.upper()
print(b(a))'''

'''a= lambda a:a.upper()
print(a("codegnan"))'''

#a="python course"
#Python Course
'''a=input()
b=lambda a:a.title()
print(b(a))'''

#firstname+lastname=fullname
'''fname=input("Enter first name:")
lname=input("Enter last name:")
fullname=lambda fname,lname:(fname+" "+lname).title()
print(fullname(fname,lname))'''

'''fname,lname=[x for x in input("Enter the fname and lname:").split(" ")]
fullname=lambda fname,lname:(fname+" "+lname).title()
print(fullname(fname,lname))'''

#filter()
#a=[10,30,50,100,127,39,45,67,200]
'''if a%2==0:
    print(a)'''
    
'''for i in a:
    if i%2==0:
        print(i)'''

'''a=[10,30,50,100,127,39,45,67,200]
b=list(filter(lambda i:i%2==0,a))
print(b)'''

#[],(),{}
'''a=[]
print(type(a))

b=()
print(type(b))

c={}
print(type(c))

d=set()
print(type(d))'''

'''a=[[],(),{}," ",None,5,6.7,"python",4+9j,True,False]
b=list(filter(None,a))
print(b)'''






































