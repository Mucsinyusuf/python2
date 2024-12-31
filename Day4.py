# Loops in python
# 1 While loop 

#while #condition:
    # code block
# i = 1
# while i <= 10:
#     print("Mucsin")
#     i += 1

# multiplication table
# number = int(input("enter a number"))
# i = 1

# while i <= 10 :
#     print(i*number)
#     i += 1

# Guessing game
# import random
# jackpot = random.randint(1,100)
# user_number = int(input("Enter a number "))
# conter = 1
# while user_number != jackpot:
#     if user_number < jackpot:
#         print("Wrong, Guess with a higher number")
#     else:
#         print("wrong, guess with a lower number ")
        
#     user_number = int(input("Enter a number "))
#     conter += 1
# else:
#     print("Correct guess")
#     print("Your attempt is : ", conter)


# For Loop
# for x in range (1,10):
#     print(x)



# Excersice 
# current_population = 10000

# for i in range (10,0,-1):
#     print(i, current_population)
#     current_population = current_population/1.1

# Nested for loops 
# printing unique pair numbers 
# for i in range(1,5):
#     for j in range(1,5):
#         print(i,j)
        
# excersice pattaern printing
# row = int(input("Enter number of rows "))
# for i in range(1,row+1):#+1 adds one increment to meet the exact number from user 
#     for j in range(1,i+1):
#         print('*', end="")
#     print("")

# Loop control statement
# Break , Continue, Pass
# Break
# for i in range(1,10):
#     if i == 5:
#         break
#     print(i)

# find prime numbers in a arange
# lower = int(input("Enter lower range "))
# upper = int(input("Enter upper range "))

# for i in range(lower, upper+1):
#     for j in range(2,i):
#         if i % j == 0:
#             break
#         else:
#             print(i)

# continue 
for i in range(1,10):
    if i == 5:
        continue
    print(i)
    
   
# pass
for i in range(1,10):
    pass