# printing in python 
print("My name is mucsin !")
print ("mucsin", end="-")
print ("Yusuf")

#Data types

# Integer 
# is a number without any deciml point 
# forexample 
print (f"3" + "is an integer  ")

# Float 
# Numbers with decimals 
# forexample 
print (f"3.14" + "Is a float ")



# Boolean
# is a true or false 
#forexample 
print(True)



# String
# Is a text 
# forexample 
print("this is a string type")



# Complex
#Is a complex type data ie a complex number
# forexample 
print (type(5+9j))

# List = []
# a list of values 
print (type([1,2,3,4]))



# Tuple = ()
print (type((1,2,3,4,5)))

# Sets = {}
print (type({1,2,3,4}))


# Dictionary = {}
print({"Name":"moha", "age":23 ,"Gender":"male"})
print (type({"Name":"moha", "age":23 ,"Gender":"male"}))


# Variables 
a = 2
print(type(a))

b = 3.5
print(type(b))

c = True
print(type(c))

d = ("mucsin")
print(type(d))

e = 4j
print(type(e))

# dynamic typing 
# example 
x = 3

# static typing 
# example 
# int y = 4

# dynamic binding 
# you can change the value for the variable 
# static binding
# once a variable is declared you cannot change it again 

z,n,m = 1,3,6
print(z,n,m)


a = b = c = 5
print(a,b,c)


# KeyWords
# are words interpreted by the interpreter
# identifiers
# are ways of declaring variables

# python inputs
# x = input ("what is your name ")
# print (f"hi" + " " + x)




# type conversion
# implicit type conversion and explcit 
# implicit is by python while explicit is by programmer
 # simple calc
# num1 = int(input("enter first_number"))
# num2 = int(input("Enter second number"))
# print(num1 + num2)


#operaters
# arithmetic operators
print(2+3)# Addition
print(3-2)# subraction
print(4/2)# division
print(4//2)# int division
print(2*3)#multiplication
print(4%2)# modulors


# relational operators
print(8>2)#greater than sign
print(4<7)#less than
print(4==4)# equal to
print(3!=4)# not equal to



# logical 
print (1 and 0)# and operator
print (1 or 0) # Or operator
print (not 1 )#not operator


# bitwise
print(2 & 1)# bitwise and
print(2 | 3 )#bitwise or
print(2 ^ 3)#bitwise xor
print(~3)# bitwise not
print(4 >> 2)#right shift
print(5 << 2)#left shiftw

# Assignment 
# = Assignment operator
# ++ increment
# -- decrement
# += 
# -=

# membership 
# in/not in
print('m' in "mucsin") #= True
print('m' not in "mucsin") # = False
print(10 not in [1,2,3,4,5])

# excercise 
# find the sum of a 3 digit number entered by user 

number = int(input("enter 3 numbers"))
a = number%10
number = number//10
b = number%10
number = number//10
c = number%10
sum = a + b + c
print(sum)
