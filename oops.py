#oops
#syntax
'''class classname():
    #attributes
    name="yasaswini"
    age=21
    place="vja"
    def fname(method_name):
        print(statements....)
obj=classname()
obj.fname()'''

#class declaration
'''class details():
    name="yasaswini"
    age=22
    place="vja"
    def display(self):
        print(self.name,self.age,self.place)
a=details()
print(dir(a))
a.display()'''

#object instantiation
'''class details():
    def data(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def display(self):
        print(self.name,self.age,self.place)
a=details()
print(dir(a))
a.data("yasaswini",22,"vja")
a.display()
b=details()
b.data("priya",24,"hyd")
b.display()
c=details()
c.data("sunitha",21,"vja")
c.display()'''

#object initialization
'''class Details():
    #creating a constructor
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def display(self):
        print(self.name,self.age,self.place)
a=Details("yasaswini",21,"vja")
print(dir(a))
a.display()'''

#Task
#Runtime Input
#method-1
'''class Details():
    #creating a constructor
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def display(self):
        print(self.name,self.age,self.place)
a=Details(input("name:"),int(input("age:")),input("place:"))
print(dir(a))
a.display()'''
#method-2
'''class Details():
    #creating a constructor
    def __init__(self):
        self.name=input("name:")
        self.age=int(input("age:"))
        self.place=input("place:")
    def display(self):
        print(self.name,self.age,self.place)
a=Details()
print(dir(a))
a.display()'''

#Difference Between _ and __
'''class Employee1():
    def __init__(self):
        self.name="yashu"
        self._mailid="yashu@gmail.com"
        self.__salary=30000#private variable
class Employee2():
    def __init__(self):
        self.name="hari"
        self._mailid="hari@gmail.com"
        self.__salary=40000#private variable
a=Employee1()
print(dir(a))
print(a.name)
print(a._mailid)
#print(a.__salary)#error
print(a._Employee1__salary)
b=Employee2()
print(dir(b))
print(b.name)
print(b._mailid)
#print(b.__salary)#error
print(b._Employee2__salary)'''

#polymorphism
#operator overloading
'''a=2;b=8
print(a+b)
print(a.__add__(b))
print(a.__add__(4))
print(a.__sub__(1))
print(a.__mul__(5))
#print(a.__div__(3))
print(a.__pow__(2))
print(a.__eq__(2))
print(a.__le__(5))
print(a.__ge__(10))
print(a.__ge__(1))
a=[2,3,4,5,6];b=[6,7,8,9,10]
print(a.__add__(b))
print(a.__getitem__(3))
print(b.__getitem__(4))
a="code";b="gnan"
print(a.__add__(b))
a="python";b="course"
print(a.__add__(" "+b))
print("yasaswini".__add__(" "+"abburi").title())'''

#operator overriding
'''class A():
    def __init__(self,a):
        self.a=a
    def __add__(self,value):
        return self.a*value.b
class B():
    def __init__(self,b):
        self.b=b
x=A(4)
y=B(5)
#x=4
#y=5
print(x+y)'''

#method overloading
'''class new():
    def sum(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            print("The sum is",a+b+c)
        elif a!=None and b!=None:
            print("The product is",a*b)
        else:
            print("The program ends......")
x=new()
x.sum()
x.sum(2,4,5)
x.sum(8,4)'''

'''class new():
    def sum(self,a=3,b=9,c=2):
        if a!=9 and b!=9 and c!=5:
            print("The sum is",a+b+c)
        elif a!=1 and b!=8:
            print("The product is",a*b)
        else:
            print("The program ends......")
x=new()
x.sum()'''
#method overriding
'''class Animal():
    def speak(self):
        print("Animals can make sounds")
class Dog():
    def speak(self):
        print("Dog can barks")
a=Animal()
b=Dog()
a.speak()
b.speak()'''

'''class car():
    def vehicle(self):
        print("Maruti")
class bike():
    def vehicle(self):
        print("Honda")  
a=car()
b=bike()
a.vehicle()
b.vehicle()'''

#inheritance()
#single-inheritance()
'''class RBI():#parent class
    cash=100000
    def available_cash(cls):
        #print("available_cash is",cls.cash)
        print("available_cash is",RBI.cash)
class SBI(RBI):#child class-1
    pass
class HDFC(RBI):#child class-2
    cash=50000
    def new_cash(cls):
        #print("new_cash is",cls.cash+cls.cash)
        print("new_cash is",cls.cash+RBI.cash)
a=HDFC()
a.available_cash()
a.new_cash()'''
#multiple-inheritance()
#task
'''class Father():#parent class-1
    weight=80
    def father_weight(cls):
        print(f"Weigth is {cls.weight} kgs")
class Mother():#parent class-1
    height=60
    def mother_height(cls):
        print(f"Height is {cls.height} inches")
class Kid(Father,Mother):#child class
    dob="27-04-2005"
    def kid_dob(cls):
        print("date of birth is",cls.dob)
a=Kid()
a.father_weight()
a.mother_height()
a.kid_dob()'''

'''class father():
    def weight(self):
        print("60kgs")
class mother():
    def height(self):
        print("5.5 inches")
class kid(mother,father):
    def dob(self):
        print("just born...")
c=kid()
c.weight()
c.height()
c.dob()'''





        
    
























