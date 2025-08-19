# ''' Control Flow in Python
#     Control flow refers to the order in which statements are executed in a program.
#     Instead of always running line by line, control flow allows your program to:
#         Make decisions (choose one path or another, explore alternatives)
#         Repeat actions (loops)
#         Exit or skip parts of code
#     It is the foundation for logic and problem solving in programming
#     Control flow is divided into 3 parts
# '''
# # A.  Conditional Statements
# #1. if Statement
# #   Executes a block only when a condition is true.
# age = 20
# if age >= 18:
#     print("You are eligible to vote")

# '''
# some usecases
#     checking for eligibility
#     validating login attempts
#     ensuring a minimum purchase requirement, etc.
# '''

# #2. if-else Statement
# #   provides two alternative paths.
# wallet = 400
# price = 500
# if wallet >= price:
#     print("Purchase successful")
# else:
#     print("Insufficient balance")

# '''
# some usecases
#     deciding success or failure of a payment.
#     granting or denying access to a system.
#     determining pass/fail in an exam, etc.
# '''
# #3. if-elif-else Statement
# #   used for multiple conditions
# score = 85
# if score >= 70:
#     print("Grade A")
# elif score >= 50:
#     print("Grade B")
# else:
#     print("Grade C")

# '''
# some usecases
#     student grading systems.
#     assigning ticket categories (VIP, Regular, Student).
#     categorizing temperatures (Hot, Warm, Cold), etc.
# '''
# #4. Nested if
# #   placing an if inside another if
# age = 19
# citizen = True

# if age >= 18:
#     if citizen:
#         print("You can vote")
#     else:
#         print("You must be a citizen to vote")
# else:
#     print("Too young to vote")

# ''' Some usecases
#     Voting eligibility (age + citizenship).
#     Banking (account active + balance sufficient).
#     School admission (age + grade level).
# '''

# #B. Loops
# ''' 1.  for loop
#         This is used for iterating over a sequence (strings, list, tuple, dictionary)
# '''
# # Iterates through each element in a list
# fruits = ["apple", "banana", "orange"]
# for fruit in fruits:
#     print(f"I like {fruit}")

# '''
# some usecases
#     Iterating through shopping lists
#     Checking availability of products
#     Displaying student names, etc.
# '''

# # Iterates through each element in a TUPLE. This works like lists, but remember that tuples are immutable.
# coordinates = (0.34654, -0.48585, 0.57477)
# for point in coordinates:
#     print(f"Point: {point}")
# '''
# Some usecases
# storing fixed sensor readings.
# displaying fixed seating positions, etc.
# '''

# # Iterates through each element in a DICTIONARY. Remember that dictionary have key:value pair
# student = {"name": "Tunde", "age": 16, "grade": "A"}
# for key, value in student.items():
#     print(f"{key}: {value}")
# '''
# some usecases
#     Reading database records.
#     showing user profile details.
#     checking configuration settings, etc.
# '''

# Iterates through each element in a STRING. Remember that strings are sequences or characters.
word = "PYTHON"
for char in word:
    print(char)
'''
some usecases
    counting vowels/consonants.
    password validation (checking digis/special chars.
    text analysis, etc.
)'''