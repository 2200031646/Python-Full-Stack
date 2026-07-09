#voting
'''age = int(input())
if age>=18:
    print("Eligible for voting")
else:
    print("Not eligible for voting")'''
#even or odd
'''num = int(input())
if num%2==0:
    print("it is even")
else:
    print("it is odd")'''
#leap year or not
'''year = int(input())
if year%4==0:
    print("it is leap year")
else:
    print("it is not leap year")'''
#guest code
'''name = "yasaswini"
name1 = input("enter the name:")
if name1==name:
    print("Welcome yasaswini")
else:
    print("Welcome guest")'''

'''name = input("enter the name:").lower()
if name=="yasaswini":
    print("Welcome",name)
else:
    print("Welcome guest")'''
#multiple users
'''names = ["yashu","siri","sindhu","kavya","hari"]
a = input("enter the name:")
if a in names:
    print("Welcome",a)
else:
    print("Welcome guest")'''
#vowels
'''vowel = ["a","e","i","o","u"]
b = input("enter the letter:").lower()
if b in vowel:
    print("It is vowel")
else:
    print("it is consonent")'''
#social-media-login
#use only nested if
'''username = input("enter the username:")
password = input("enter the password:")
if username == password:
    print("Login successful")
    if username != password:
        print("Invalid credentials")
else:
    print("Invalid credentials")'''

'''username = input("enter the username:")
password = int(input("enter the password:"))
if username == "yasaswini":
    if password == 1234:
        print("Login successful")
    else:
        print("Invalid password")
else:
    print("Invalid username")'''

'''a="yasaswini"
b=1234
username = input("enter the username:")
password = int(input("enter the password:"))
if username == a:
    if password == b:
        print("Login successful")
    else:
        print("Invalid password")
else:
    print("Invalid username")'''
#using if-else
'''username = input("enter the username:")
password = input("enter the password:")
if username == "yasaswini" and password == "yashu@1234":
    print("Login successful")
else:
    print("Invalid credentials")'''

'''username = input("enter the username:")
password = int(input("enter the password:"))
if username == "yasaswini" and password == 1234:
    print("Login successful")
else:
    print("Invalid credentials")'''
#multiple if

'''age = int(input("enter age:"))
marks = int(input("enter marks:"))
attendence = int(input("enter attendence:"))
if age>=18:
    print("Eligible for vote")
if marks>=80:
    print("Eligible for scholarship")
if attendence>=70:
    print("Allow to write exams")'''

#if-elif-else
#Bakery
'''cake = int(input("enter the price:"))
if cake == 1200:
    print("redvelvet cake")
elif cake == 1000:
    print("almond cake")
elif cake == 800:
    print("chocolate cake")
elif cake == 600:
    print("butter scotch cake")
else:
    print("cake is not available")'''

#Pizza
'''pizza = input("enter the name:")
if pizza == "bbq pizza":
    print("Price is 800")
elif pizza == "crispy chicken pizza":
    print("prince is 600")
elif pizza == "paneer pizza":
    print("prince is 400")
elif pizza == "corn pizza":
    print("prince is 200")
elif pizza == "frenchfries & coke":
    print("price is 150")
else:
    print("not available")'''

'''pizza = input("enter the name:")
if pizza == "bbq pizza":
    print(800)
elif pizza == "crispy chicken pizza":
    print(600)
elif pizza == "paneer pizza":
    print(400)
elif pizza == "corn pizza":
    print(200)
elif pizza == "frenchfries & coke":
    print(150)
else:
    print("not available")'''




























