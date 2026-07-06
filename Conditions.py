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


