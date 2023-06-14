# a = 2;
# b = 3;
# print (a is b)

# a = {1,2,3,4,5,6}
# print (3 in a)

# #Memebership Operator in and not in
# list = ['Apple', 'Pie', 'Grapes']
# print ('Apple' in list)

# #Membership Operator String Example 
# str1 = 'Dipesh'
# print ('D' in str1)

#if statement

# a = 4,
# b=5,

# if (a > b):
#     {
#     print ("A is greater than B")
# }
# else:{
#     print ("B is greater than A")
# }


# num= 5;
# if num>5:
#     {
#         print("Number is greater than 5")
#     }
# elif num<5:
#     {
#         print ("NUmber is less than 5")
#     }
# else: (
#     print ("Number is 5")
# )


# num= 6;
# if num>5:
#     {
#         print("Number is greater than 5")
#     }
# if num<5:
#     {
#         print ("NUmber is less than 5")
#     }
# if num == 5: (
#     print ("Number is 5")
# )

# age = 12;

# if age >18:
#     {
#         print("Eligible to vote")
#     }
    
# else:{
#       print("NOt eligible to vote")  
#     }



# num1=10
# if num1<10 :
#     print ("Number is less than 1")

# elif num1>10 and num1%2==0:
#     print("Number is even and greater than 10")

# else:
#     print ("Number is odd and greater than 10")


# age= int(input("Enter the age:"))

# if ( age>0 and age<18):
#     flag = 1
#     print ("underage")
    
# elif (age>= 18 and age < 25):
#     flag = 1
#     print ("Student")
    
# elif (age>= 25 and age <= 55):
#     flag = 1
#     print("Working adult")
    
# elif (age > 55):
#     flag = 1
#     print("Oldage")
    
# else:
#     flag = 0
#     print("Invalid Data")
    
# if flag == 1:
# print("This gives us age group")

# else:
# print ("Invalid Entry:")

# number = int ( input ("Enter a number"))

# if (number > 10):
#     print ("Number is greater than 10")
    
#     if (number%2 is 0):
#         print("Number is greater than 10 and is even")
        
#     elif (number< 10):
#         print ("Number is less than 0")    
# else:
#     print ("Number is odd")

# fruit_list = ['Apple', 'Banana', 'Cherry']
# # list is iterable
# for items in fruit_list:
#     print (items)

# for numbers in range(5,10):
#     print(numbers)
    

# list = [0,1,2,3,4,5]
# sum  = 0
# for items in list:
#     sum += items
#     print(sum)
    

# a = 100
# while a >= 1:
#     print("Value is", a)
#     a -= 1

# a = 11
# while a > 6:
#     a -= 1
#     if a == 5:
#         continue
#     print(a)


# multiple = 0
# num = 1

# while multiple < 5:
#     if num % 6 == 0:
#         print("6 X",multiple, '=',num)
#         multiple += 1
#     num += 1

# num = 1
# while num <= 10:
#     if num % 2 != 0:
#         num += 1
#         continue
#     print(num)
#     num += 1


# Homework1
i = 2
n = 50
j = 2
flag = 1
primes_list = []

while i <= n:

    flag = 1  # Reset flag to 1 before each inner loop starts

    while j <= i / 2:
        if i % j == 0:
            flag = 0
            break
        j += 1

    if flag == 1:
        primes_list.append(i)

    i += 1
    j = 2

print(primes_list)

#Homework2
unit = int(input("Enter number of units: "))

if unit <= 100:
    charge = 0
elif unit <= 200:
    charge = (unit - 100) * 5
else:
    charge = 100 * 5 + (unit - 200) * 10

print("Your total electricity bill is:", charge)

