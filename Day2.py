# if/else conditional statement
email = input("Enter your email")
password = input("Enter password")

if email == 'mucsin@gmail.com' and password == 'Alhamdulillah' :
    print("Login Successfull")
elif email == 'mucsin@gmail.com' or password == 'Alhamdulillah':
    print("try with another credentials")
else:
    print("Wrong password")


# nested if/else condition
if email == 'mucsin@gmail.com' and password == 'Alhamdulillah' :
    print("Login Successfull")
elif email == 'mucsin@gmail.com' or password != 'Alhamdulillah':
    print("try with another credentials")
    password = input("Enter password again")
    if password :
        print("Success")
    else:
        print("Wrong")
else:
    print("Wrong password")



# Excersice
# find the min of three numbers
num1 = int(input("Enter first number ")) 
num2 = int(input("Enter second number "))
num3 = int(input("Enter third number "))
if num1 < num2 and num1 < num3 :
    print(f"{num1}" + " " "is the min")
elif num2 < num1 and num2 < num3 :
    print(f"{num2}" + " " "is the min")
elif num3 < num1 and num3 < num2:
    print(f"{num3}" + " " "is the min")

# excersice 2
# ATM Machine menu

menu =  input("""
hi there welconme 
please choose ;
             1. Enter 1 for pin change
             2. Enter 2 to check balance
             3. Enter 3 for withdraw
             4. Enter 4 for Deposit
             5. Enter 5 for Exit

""")
if menu == '1':
    print("Pin change")
elif menu == '2':
    print("Balance check")
elif menu == '3':
    print("Withdrawal")
elif menu == '4':
    print('Deposit')
else:
    print("exit")