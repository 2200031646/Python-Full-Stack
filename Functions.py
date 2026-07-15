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
                 
    


















































