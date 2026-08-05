#Email Automation
import random
import math
import smtplib #Simple Mail Transfer Protocol library

digits="0123456789"
OTP="" #Empty string

for i in range(6):
    OTP+=digits[math.floor(random.random()*10)]
otp=OTP+" is your otp"
msg=otp
                
s=smtplib.SMTP("smtp.gmail.com",587)
s.starttls()
s.login("your_email@gmail.com", "your_app_password") #Gmail App Password
user="your_email@gmail.com"

emailid=input("enter the mail which you want to send otp:")
s.sendmail(user,emailid,msg)

while True:
    a=input("enter the otp:")
    if a==OTP:
        print("otp is correct")
    else:
        print("incorrect otp")





        
