# Basic usage of input()
'''
name = input("Enter your name: ")
print ("Hello,", name)
print ("Hello, " + name) #concatenation

age = int(input("Enter your age: "))
print (f"You will be {age + 1} years old next year.") # with f-string
print ("You will be", age + 1, "years old next year.") # without f-string

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
sum_result = num1 + num2
print (f"The sum of {num1} and {num2} is {sum_result}.")
print ("The sum of", num1, "and", num2, "is", sum_result, ".")
'''

# name = input ("My name is ")
# print ("\n Hello,", name)
# print ("Welcome to NCC Restaurant")

# print ("\n What would you like to order?")
# order = input ("I would like to order: ")

# print ("\n You order", order)
# print ("Your order is ready \n Thank you!")

# Step 1
# Step 2
# Step 3
# Step 4

# age = int(input("Enter your age: "))
# print (f"You will be {age + 1} years old next year.") # with f-string
# print ("You will be", age + 1, "years old next year.") # without f-string


# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))
# sum_result = num1 + num2
# print (f"The sum of {num1} and {num2} is {sum_result}.")
# print ("The sum of", num1, "and", num2, "is", sum_result, "\b.")



# Input USSD
# Selecting options
# Another option

print ("Welcome to Airtel Ng Services")
ussd = input("Input code: ")
print ("Select options: \
       \n1. Buy Bundles \
       \n2. Manage Data \
       \n3. Borrow \
       \n4. View Tariffs \
       \n5. Last Recharge \
       \n# Next \
       \nReply")
option = input("Select option: ")
print (f"You choose option {option}")
print ("Sorry\nWe cannot proceed with this service")