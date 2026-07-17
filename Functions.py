#Functions
#without function
'''a=10
b=20
print("The sume is:",a+b)
print("The diff is:",a-b)
print("The product is:",a*b)
a=100
b=200
print("The sume is:",a+b)
print("The diff is:",a-b)
print("The product is:",a*b)
a=1000
b=2000
print("The sume is:",a+b)
print("The diff is:",a-b)
print("The product is:",a*b)'''
#Using Functions
#Arithmetic Operations
'''def calculate(a,b):
    print("The sume is:",a+b)
    print("The diff is:",a-b)
    print("The product is:",a*b)
calculate(10,20)
calculate(100,200)
calculate(1000,2000)'''

'''def calculate(a,b):
    print("The integer division is:",a//b)
    print("The power is:",a**b)
    print("The modulus is:",a%b)
calculate(10,20)
calculate(2,4)
calculate(5,6)'''
#Addition Function
'''def add(a,b):
    print(a+b)
add(4,6)'''
#user input
'''def cal():
    a=int(input("a value:"))
    b=int(input("b value:"))
    print(a+b)
cal()'''
#using while loop
'''while True:
    def cal():
        a=int(input("a value:"))
        b=int(input("b value:"))
        print(a+b)
    cal()'''
#using recursive function
'''def cal():
    a=int(input("a value:"))
    b=int(input("b value:"))
    print(a+b)
    cal()
cal()'''

'''def fullname():
    fname=input("first name:")
    lname=input("last name:")
    print((fname+" "+lname).title())
fullname()'''

'''def mul(a,b):
    print(a*b)
mul(3,5)'''

'''def mul(a,b):
    return a*b
print(mul(2,3))'''
#print v/s return
'''def add(a,b):
    c=a+b
    d=a-b
    e=a*b
    print(c)
    print(d)
    print(e)
add(5,6)'''

'''def add(a,b):
    c=a+b
    d=a-b
    e=a*b
    #return c
    #return d
    #return e
    return c,d,e
print(add(3,4))'''
#splitbill()
'''def splitbill():
    bill = int(input("Total bill:"))
    people = int(input("Total num of people:"))
    print(bill//people)
splitbill()'''

'''def splitbill():
    bill = int(input("Total bill:"))
    people = int(input("Total num of people:"))
    split = bill//people
    print(f"The split is {split}")
    print("The split is {}".format(split))
splitbill()'''

'''def splitbill():
    bill = int(input("Total bill:"))
    people = int(input("Total num of people:"))
    print(f"The split is {bill//people}")
    print("The split is {}".format(bill//people))
splitbill()'''
# Menu-Driven Calculator Function
'''while True:
    def operation():
        a = int(input("The a value is:"))
        b = int(input("The b value is:"))
        option = int(input("Enter the option:1.add 2.sub 3.div"))
        if option==1:
            print(f"The addition is:{a+b}")
        elif option==2:
            print(f"The subtraction is:{a-b}")
        elif option==3:
            print(f"The division is:{a/b}")
        else:
            print("Invalid option")
    operation()'''

#multiple def
'''def add():
    print(a+b)
def sub():
    print(a-b)
def mul():
    print(a*b)
while True:
    a = int(input("The a value is:"))
    b = int(input("The b value is:"))
    option = int(input("Enter the option:1.add 2.sub 3.div"))
    if option==1:
        add()
    elif option==2:
        sub()
    elif option==3:
        mul()'''
# Keyword and Positional Arguments
'''def Details(id,name,mailid):
    id=10
    name="yasaswini"
    mailid="yasaswini.abburi@gmail.com"
    print(id,name,mailid)
Details(id="id",name="name",mailid="mailid")'''


'''def Details(id,name,mailid):
    print(id,name,mailid)
Details(id="id",name="name",mailid="mailid")
Details(id=20,name="sita",mailid="sita@gmail.com")
Details(id=30,name="rama",mailid="rama@gmail.com")
Details(40,"arshitha","arshi@gmail.com")
Details("suni@gmail.com",50,"sunitha")
Details(mailid="satya@gmail.com",id=60,name="satya")'''
# Default Arguments
'''def Grocery(item,price):
    print("item is %s" %item)
    print("price is %.2f" %price)
Grocery("sugar",100)'''

'''def Grocery(item="rice",price=1500):
    print("item is %s" %item)
    print("price is %.2f" %price)
Grocery()'''

'''def Grocery(item,price=200):
    print("item is %s" %item)
    print("price is %.2f" %price)
Grocery("dhal")'''
#A Non-default Argument Cannot Follow a Default Argument
'''def Grocery(item="ghee",price): 
    print("item is %s" %item)
    print("price is %.2f" %price)
Grocery(500)'''

#task
'''def bakery(cake_name,price,qty):
    print("cake is %s" %cake_name)
    print("price is %.2f" %price)
    print("quantity is %d kg/g" %qty)
bakery("dark chocolate",2000,1)'''

'''def bakery(cake_name="butter scotch",price=2500,qty=2):
    print("cake is %s" %cake_name)
    print("price is %.2f" %price)
    print("quantity is %d kg/" %qty)
bakery()'''

'''def bakery(cake_name,price=3500,qty=3):
    print("cake is %s" %cake_name)
    print("price is %.2f" %price)
    print("quantity is %d kg/g" %qty)
bakery("black forest")'''
#non def arg follows def arg
'''def bakery(cake_name="red velvet",price=3500,qty): 
    print("cake is %s" %cake_name)
    print("price is %.2f" %price)
    print("quantity is %d kg/g" %qty)
bakery(3)'''

# * arguments(* is used to unpack the elements)
# Unpacking a List
'''a=[2,3,4,5,6,7]
print(a)
print(*a)'''
# Unpacking a Tuple
'''a=(2,3,4,5,6,7)
print(a)
print(*a)'''
# Unpacking a Set
'''a={2,3,4,5,6,7}
print(a)
print(*a)'''
# Unpacking Dictionary Keys
'''b={"name":"yashu","city":"vij"}
print(b)
print(*b)'''
# Unpacking a String
'''c="python"
print(c)
print(*c)'''
# Incorrect Multiple Assignment (Too Many Values)
'''a,b,c=2,3,4,5,6,7,8,9,10
print(a)
print(b)
print(c)'''#error
# Correct Multiple Assignment
'''a,b,c=2,3,4
print(a)
print(b)
print(c)'''
# Using * with Multiple Assignment
'''*a,b,c=2,3,4,5,6,7,8,9,10
print(*a)
print(b)
print(c)'''
# Incorrect String Unpacking
'''a,b,c="codegnan"
print(a)
print(b)
print(c)'''#error
# Correct String Unpacking
'''a,b,c="cod"
print(a)
print(b)
print(c)'''
# Using * to Unpack Characters from a String
'''a,*b,c="codegnan"
print(a)
print(*b)
print(c)'''

#variable length arguments
'''def check(*a):
    print(a)
    print(type(a))
check()
check(2,3,4,5,6,7,8)
b=[4,5,6,7,8]
check(*b)
c={5,6,7,8,9,10}
check(*c)
d={"name":"pooja","age":28,"place":"vja"}
check(*d)'''

'''def check1(*a):
    d=1#creating a variable
    print(a)
    print(type(a))
    for i in a:
        if type(i) in (int,float):
            d=d+i
            print(d)
check1()
check1(2,3,4,5,6)
check1(1,3,4,5,2.3,4.3)
check1(4,3,6,2,3.4,2.3,"python",4+9j,True,False)'''

#**(kwargs)-keyword variable length arguments
'''def check2(**a):
    print(a)
    print(type(a))
check2()
details={"names":["sweety","viji","vani"],
         "marks":[60,70,80],
         "status":["p","a","p"]}
check2(**details)'''

'''def check2(**a):
    print(a)
    print(type(a))
    for i in a:
        print(i)
    for i in a.keys():
        print(i)
    for i in a:
        print(a[i])
    for i in a.values():
        print(i)
    for i in a:
        print(i,a[i])
    for i in a.items():
        print(i)
check2()
details={"names":["sweety","viji","vani"],
         "marks":[60,70,80],
         "status":["p","a","p"]}
check2(**details)'''

# Both * and ** usage
'''def final(*a,**b):
    d=2
    print(a)
    print(b)
    print(type(a))
    print(type(b))
    for i in a:
        d=d+i
        print(d)
    for i,j in b.items():
        print("key is",i)
        print("value is",j)
final()
data=(2,3,4,5,6,3.5,7.8)
final(*data)
details={"year":[2026,2027,2028],
         "month":["june","july","aug"]}
final(**details)
final(*data,**details)'''


            
        
        
























