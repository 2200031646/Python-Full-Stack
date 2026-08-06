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
























