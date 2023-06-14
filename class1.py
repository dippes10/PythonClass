# #this is my first python class

# print ("Hello World!")

# name, age, height, position = "Dipesh Sanjel", 22 , 173, "CEO"
# print ( name, age, height, position )

# name = sname = "Sanjel"

# print ( name, sname)

# PI = 3.14
# GRAVITY = 9.8
# print (PI)

# rollNo = 7
# print ( type ( rollNo ) )

# height = 173
# print ( type ( height ) )

# name = 'Dipesh'
# print ( type (name) )

# complex = 2 + 3j
# print ( type (complex) )

# myValue = None;
# print ( type ( myValue ) )

# print ( rollNo, height, name, complex, myValue )
# first_int = 123
# first_float = 1.23
# add = first_int + first_float

# print ( add, type(add))

# string = "SIRAK"
# int1= "6"

# sum = (string + int1)
# print ( sum, type(sum))

# num1 = "12"
# num1_int = int (num1)
# num2 = 34
# print ( num1_int + num2)

# ph1 = "12.34"
# ph1_float = float ( ph1 )
# ph2 = 12.34

# print ( ph1_float + ph2)

#e1
# age = 22
# fage= 21
# print ( 'Hello!')

# #e2
# print ('My age is', age)

# print ( 'I am {} years old'.format(age))

# print ("I am ",+age," years old and my friend's age is ",+fage)

# myage = ("Enter your age:")
# print (myage)
# print (type(myage))

# name = input("Enter your Name:")
# age = input("Enter your age:")
# height =input ("Enter your height")

# age1 = int (age)
# height1 = float (height)

# print ( "My name is", "My age is",age1, "My height is", height1)
# print ( type (name), type(age1), type(height1))

# num1 = int (input ( "Enter the first number"))
# num2 = int (input ( "Enter the second number"))

# print ( " sum is", num1+ num2, "product is", num1*num2, "Substraction is", num1-num2, "Division is", num1/num2, "Floor Division", num1//num2,"Modulo",num1%num2, "first Power second", num1 **num2)

# b=10
# a=7

# print (a)
# b += 1 
# print (a)

# c -= 4
# print (a)
# d *= 4
# print (a)

# print ( a> b)


#1
#Correct variable Names

# age
# name
# num_students
# total_sales
# is_active


#incorrect variable names

# 3people #starts with a digit
# my-variable #contains a hyphen
# first name #contains a space
# total-sales$ #contains a special character
# class  #reserved keyword



#2
# Integer:  age = 25

# Float: pi = 3.14

# String: name = "John Doe"

# Boolean:  is_raining = True

# List:  numbers = [1, 2, 3, 4, 5]

# Tuple:  coordinates = (10, 20)

# Dictionary: student = {"name": "John", "age": 20}

# Set: colors = {"red", "green", "blue"}

# None : result = None

# Complex:  z = 2 + 3j



#3

user_input = input("Enter a number: ")
number = int(user_input)
result = number * 5
print("The result is:", result)



#4

# Taking input from the user
name = input("Enter your name: ")
phone_num = input("Enter your phone number: ")
address = input("Enter your address: ")
is_married = input("Are you married? (True/False): ")

# Type conversion
phone_num = int(phone_num)
is_married = bool(is_married)

# Output
print("Name:", name, "Type:", type(name))
print("Phone number:", phone_num, "Type:", type(phone_num))
print("Address:", address, "Type:", type(address))
print("Is married:", is_married, "Type:", type(is_married))


#4

# Assignment Operators
x = 100
y = 10  

# Arithmetic Operators
addition = x + y         # Adds x and y
subtraction = x - y      # Subtracts y from x
multiplication = x * y   # Multiplies x and y
division = x / y         # Divides x by y
modulus = x % y          # Returns the remainder of x divided by y
exponentiation = x ** y  # Raises x to the power of y
floor_division = x // y  # Returns the integer part of the division of x by y

# Output
print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)
print("Modulus:", modulus)
print("Exponentiation:", exponentiation)
print("Floor Division:", floor_division)
