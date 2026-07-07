#Conditions
#if-condition by using comparision operators
#<,>,<=,>=,!=,==
'''a=4
b=8
if a<b:
    print("true")'''

'''a=7
b=10
if a>b:
    print("true")'''

'''a=6
b=9
if a<=b:
    print("less")'''

'''a=12
b=15
if a>=b:
    print("true")'''

'''a=20
b=30
if a!=b:
    print("True")'''

'''a=9
b=9
if a==b:
    print("true")'''

'''a="python"
if a=="python":
    print("match")'''

'''a=int(input("a value:"))
b=int(input("b value:"))
if a<b:
    print("less")'''

'''a=int(input("a value:"))
if a<50:
    print("less")'''

#if condition by using logical operators
#and,or,not
'''a=3
b=6
if a<b and b>a:
    print("True")'''

'''a=5
b=9
if a<=b and b>=a:
    print("true")'''

'''a=9
b=12
if a!=b and a==b:
    print("true")'''

'''a=5
b=8
if a<b or b>a:
    print("true")'''

'''a=12
b=14
if a<=b or b>=a:
    print("true")'''

'''a=3
b=6
if a!=b or a==b:
    print("true")'''

'''a=5
b=7
if not a<b:
    print("true")'''

'''a=4
b=7
if not a>b:
    print("true")'''

'''a=5
b=7
if not a<b and b>a:
    print("true")'''

'''a=3
b=6
if not a<b or b>a:
    print("true")'''

#if-condition by using identify operators
#is,is not
'''a=4
if type(a) is int:
    print("is is int")'''

'''a=4
if type(a) is not int:
    print("is is int")'''

'''a=4.5
if type(a) is float:
    print("is float")'''

'''a=3.4
if type(a) is not float:
    print("is float")'''

'''a="hi"
if type(a) is str:
    print("is string")'''

'''a="hi"
if type(a) is not str:
    print("is string")'''

'''a=3+6j
if type(a) is complex:
    print("is complex")'''

'''a=4+2j
if type(a) is not complex:
    print("is complex")'''

'''a= True
if type(a) is bool:
    print("is bool")'''

'''a= True
if type(a) is not bool:
    print("is bool")'''

#if-condition by using membership operators
#in,not in
'''a=2,3,4,5,6,7,8
if 8 in a:
    print("True")'''

'''a=2,3,4,5,6,7,8
if 20 not in a:
    print("True")'''

'''a=int(input("a value:"))
if 30 in a:
    print("true")''' #error

'''a=2,3,4,5,6,7,8,9,10
b=int(input("value:"))
if b in a:
    print("true")'''

#if-else
#if-else condition by using comparision operators

'''a=4
b=9
if a<b:
    print("True")
else:
    print("False")'''
      
'''a=4
b=9
if a>b:
    print("True")
else:
    print("False")'''

'''a=5
b=10
if a<=b:
    print("less")
else:
    print("False")'''

'''a=5
b=10
if a>=b:
    print("less")
else:
    print("False")'''

'''a=5
b=10
if a!=b:
    print("True")
else:
    print("False")'''

'''a=10
b=10
if a==b:
    print("True")
else:
    print("False")'''

'''a="Yasaswini"
if a=="Hi":
    print("match")
else:
    print("False")'''

'''a=int(input("a value:"))
b=int(input("b value:"))
if a<b:
    print("True")
else:
    print("False")'''

'''a=int(input("a value:"))
if a<20:
    print("True")
else:
    print("False")'''

#if-else condition by using logical operators

'''a=10
b=22
if a<b and b>a:
    print("True")
else:
    print("False")'''

'''a=33
b=34
if a<=b and b>=a:
    print("True")
else:
    print("False")'''

'''a=3
b=7
if a!=b and b==a:
    print("True")
else:
    print("False")'''

'''a=7
b=19
if a<b or b>a:
    print("True")
else:
    print("False")'''

'''a=23
b=25
if a<=b or b>=a:
    print("True")
else:
    print("False")'''

'''a=3
b=11
if a!=b or b==a:
    print("True")
else:
    print("False")'''

'''a=12
b=17
if not a<b:
    print("true")
else:
    print("False")'''

'''a=12
b=18
if not a>b:
    print("true")
else:
    print("False")'''

'''a=4
b=11
if not a<b and b>a:
    print("true")
else:
    print("False")'''

'''a=3
b=13
if not a<b or b>a:
    print("true")
else:
    print("False")'''

#if-else condition by using identify operators

'''a=10
if type(a) is int:
    print("is int")
else:
    print("False")'''

'''a=1
if type(a) is not int:
    print("is int")
else:
    print("False")'''

'''a=1.2
if type(a) is float:
    print("is float")
else:
    print("False")'''

'''a=2.2
if type(a) is not float:
    print("is float")
else:
    print("False")'''

'''a="Hello"
if type(a) is str:
    print("is string")
else:
    print("False")'''

'''a="Hello"
if type(a) is not str:
    print("is string")
else:
    print("False")'''

'''a=2+7j
if type(a) is complex:
    print("is complex")
else:
    print("False")'''

'''a=3+6j
if type(a) is not complex:
    print("is complex")
else:
    print("False")'''

'''a=True
if type(a) is bool:
    print("is bool")
else:
    print("False")'''

'''a=True
if type(a) is not bool:
    print("is bool")
else:
    print("False")'''

'''a=int(input("value:"))
if type(a) is int:
    print("is int")
else:
    print("False")'''

'''a=float(input("value:"))
if type(a) is float:
    print("is float")
else:
    print("False")'''

'''a=str(input())
if type(a) is str:
    print("is string")
else:
    print("False")'''

#if-else condition by using membership operators

'''a=10,12,14,16,18
if 1 in a:
    print("True")
else:
    print("False")'''

'''a=21,31,41,51,6,7,1
if 20 not in a:
    print("True")
else:
    print("False")'''

'''a=9,8,7,6,5,4,3,2
b=int(input("value:"))
if b in a:
    print("True")
else:
    print("False")'''

#if-elif-else
#if-elif-else condition by using comparision operators

'''a=3
b=5
if a<b:
    print("less")
elif b>a:
    print("greater")'''

'''a=4
b=7
if a==b:
    print("less")
elif b<a:
    print("greater")
elif a!=b:
    print("not equal")'''

'''a=1
b=6
if a<b:
    print("less")
elif b>a:
    print("greater")
else:
    print("true")'''

'''a=3
b=9
if a==b:
    print("less")
elif b<a:
    print("greater")
else:
    print("true")'''
    
#if-elif-else condition by using logical operators

'''a=11
b=25
if a<b and b>a:
    print("True")
elif a>b and b<a:
    print("False")
else:
    print("invalid")'''

'''a=3
b=6
if a<=b and b>=a:
    print("True")
elif a>=b and b<=a:
    print("False")
else:
    print("invalid")'''

'''a=2
b=7
if a!=b and b==a:
    print("True")
elif b!=a and a==b:
    print("False")
else:
    print("invalid")'''

'''a=17
b=19
if a<b or b>a:
    print("True")
elif a>b or b<a:
    print("False")
else:
    print("invalid")'''

'''a=21
b=52
if a<=b or b>=a:
    print("True")
elif a>=b or b<=a:
    print("False")
else:
    print("invalid")'''

#All logical operators can be done in one code
'''a=2
b=25
if a<b and b>a:
    print("True")
elif a!=b or a==b:
    print("equal")
elif not b>a:
    print("false")
else:
    print("invalid")'''

#if-elif-else condition by using identify operators

'''a=22
if type(a) is int:
    print("it is int")
elif type(a) is not int:
    print("false")
else:
    print("invalid")'''
    
'''a=2.4
if type(a) is float:
    print("it is float")
elif type(a) is not float:
    print("false")
else:
    print("invalid")'''

'''a="hello"
if type(a) is str:
    print("it is string")
elif type(a) is not str:
    print("false")
else:
    print("invalid")'''

'''a=2+6j
if type(a) is complex:
    print("it is complex")
elif type(a) is not complex:
    print("false")
else:
    print("invalid")'''

'''a=True
if type(a) is bool:
    print("it is boolean")
elif type(a) is not bool:
    print("false")
else:
    print("invalid")'''

#if-elif-else condition by using membership operators

'''a=10,12,14,16,18
if 10 in a:
    print("True")
elif 12 not in a:
    print("False")
else:
    print("invalid")'''

#multiple-if conditions
#multiple-if conditions by using comparision operators
'''a=10
b=40
if a<b:
    print("less")
if b>a:
    print("greater")
if a!=b:
    print("not equal")'''

'''a=12
b=30
if a==b:
    print("less")
if b>a:
    print("greater")
if a!=b:
    print("not equal")'''

'''a=1
b=4
if a==b:
    print("less")
if b>a:
    print("greater")
if a>=b:
    print("not equal")
else:
    print("true")'''

#multiple-if conditions by using logical operators

'''a=21
b=25
if a<b and b>a:
    print("True")
if a!=b or a==b:
    print("equal")
if not b<a:
    print("false")
else:
    print("invalid")'''

#multiple-if conditions by using identify operators

'''a=22
if type(a) is int:
    print("it is int")
if type(a) is not int:
    print("false")
else:
    print("true")'''

'''a=2.3
if type(a) is float:
    print("it is float")
if type(a) is not float:
    print("false")
else:
    print("true")'''

'''a="hi"
if type(a) is str:
    print("it is str")
if type(a) is not str:
    print("false")
else:
    print("true")'''

'''a=2+2j
if type(a) is complex:
    print("it is complex")
if type(a) is not complex:
    print("false")
else:
    print("true")'''

'''a=22
if type(a) is bool:
    print("it is bool")
if type(a) is not bool:
    print("false")
else:
    print("true")'''

#multiple-if conditions by using membership operators

'''a=10,12,14,16,18
if 10 in a:
    print("True")
if 11 not in a:
    print("False")
else:
    print("invalid")'''

#nested-if
#nested-if conditions

'''a=7
b=9
if a<b:
    print("less")
    if b>a:
        print("greater")'''
#no output as main condition fails
'''a=6
b=10
if a>b:
    print("less")
    if b>a:
        print("greater")'''

'''a=17
b=19
if a!=b:
    print("true")
    if b==a:
        print("greater")'''

'''a=6
b=12
if a!=b:
    print("true")
    if b==a:
        print("equal")
    else:
        print("false")'''

'''a=4
b=22
if a==b:
    print("true")
    if b>a:
        print("greater")
else:
    print("false")'''

'''a=2
b=3
if a!=b:
    print("true")
    if b==a:
        print("equal")
    else:
        print("false")
else:
    print("not true")'''

'''a=14
b=17
if a!=b:
    print("true")
    if b==a:
        print("equal")
    elif a<b:
        print("less")
    else:
        print("false")'''

'''a=int(input())
b=int(input())
if a!=b:
    print("true")
    if b==a:
        print("equal")
    elif b>a:
        print("greater")
    else:
        print("false")
else:
    print("program ends")'''


