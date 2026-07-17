# Railway Ticket Application
while True:
    def railway():
        ticket=1000
        option = int(input("Enter the option:1.Male 2.Female: "))
        if option==1:
            print("Welcome sir")
            age=int(input("please enter your age:"))
            if age>=60:
                print("you got 30% discount")
                discount = ticket-(30/100*ticket)
                print(f"After discount ticket price:{discount}")
            else:
                print("No discount")
                print(f"your ticket price is {ticket}")
                
        elif option==2:
            print("Welcome mam")
            age=int(input("please enter your age:"))
            if age>=60:
                print("you got 50% discount")
                discount = ticket-(50/100*ticket)
                print(f"After discount ticket price:{discount}")
            else:
                print("you got 30% discount")
                discount = ticket-(30/100*ticket)
                print(f"After discount ticket price:{discount}")
        else:
            print("Invalid option")
    railway()
