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






































