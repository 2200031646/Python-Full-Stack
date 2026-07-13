# ATM APPLICATION 
while True:
    account = 100000
    pwd = 1234
    card = input("Insert the card: ")

    if card == "c":
        print("Welcome Yasaswini")

        password = int(input("Enter the password: "))

        if password == pwd:

            option=int(input("Choose an option 1.Bank Balance 2.Withdraw"))

            if option == 1:
                print("Your balance is:", account)

            elif option == 2:
                money = int(input("Enter the amount: "))

                if money <= account:
                    account = account - money
                    print(money,"amount is withdrawn")
                    print("Remaining balance is:", account)
                else:
                    print("Insufficient balance")

            else:
                print("Invalid option")

        else:
            print("Incorrect password")

    else:
        print("Invalid card")




