# Swapping Two Variables
# Using a Temporary Variable
'''a=10
b=20
c=0
c=a
a=b
b=c
print(a)
print(b)'''
# Swapping Without a Temporary Variable
'''a=10
b=20
a,b=b,a
print(a)
print(b)'''
# Swapping Using Arithmetic Operators
'''a=10
b=20
a=a+b
b=a-b
a=a-b
print(a)
print(b)'''
# Number Formatting (Integer)
'''a=10
b=20
a=a+b
b=a-b
a=a-b
print("after swapping a=%d,b=%d" %(a,b))'''
# Number Formatting (Float)
'''a=float(input())
b=float(input())
a=a+b
b=a-b
a=a-b
print("after swapping a=%.2f,b=%.2f" %(a,b))'''
# Number Formatting (String)
'''a=input()
b=input()
a,b=b,a
print("after swapping a=%s,b=%s" %(a,b))'''
