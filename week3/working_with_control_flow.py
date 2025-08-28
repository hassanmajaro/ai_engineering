''' Control Flow in Python
    Control flow refers to the order in which statements are executed in a program.
    Instead of always running line by line, control flow allows your program to:
        Make decisions (choose one path or another, explore alternatives)
        Repeat actions (loops)
        Exit or skip parts of code
    It is the foundation for logic and problem solving in programming
    Control flow is divided into 3 parts
'''
# A.  Conditional Statements
#1. if Statement
#   Executes a block only when a condition is true.
age = 20
if age >= 18:
    print("You are eligible to vote")

'''
some usecases
    checking for eligibility
    validating login attempts
    ensuring a minimum purchase requirement, etc.
'''

#2. if-else Statement
#   provides two alternative paths.
wallet = 400
price = 500
if wallet >= price:
    print("Purchase successful")
else:
    print("Insufficient balance")

'''
some usecases
    deciding success or failure of a payment.
    granting or denying access to a system.
    determining pass/fail in an exam, etc.
'''
#3. if-elif-else Statement
#   used for multiple conditions
score = 85
if score >= 70:
    print("Grade A")
elif score >= 50:
    print("Grade B")
else:
    print("Grade C")

'''
some usecases
    student grading systems.
    assigning ticket categories (VIP, Regular, Student).
    categorizing temperatures (Hot, Warm, Cold), etc.
'''
#4. Nested if
#   placing an if inside another if
age = 19
citizen = True

if age >= 18:
    if citizen:
        print("You can vote")
    else:
        print("You must be a citizen to vote")
else:
    print("Too young to vote")

''' Some usecases
    Voting eligibility (age + citizenship).
    Banking (account active + balance sufficient).
    School admission (age + grade level).
'''

#B. Loops
''' 1.  for loop
        This is used for iterating over a sequence (strings, list, tuple, dictionary)
'''
# Iterates through each element in a list
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(f"I like {fruit}")

'''
some usecases
    Iterating through shopping lists
    Checking availability of products
    Displaying student names, etc.
'''

# Iterates through each element in a TUPLE. This works like lists, but remember that tuples are immutable.
coordinates = (0.34654, -0.48585, 0.57477)
for point in coordinates:
    print(f"Point: {point}")
'''
Some usecases
storing fixed sensor readings.
displaying fixed seating positions, etc.
'''

# Iterates through each element in a DICTIONARY. Remember that dictionary have key:value pair
student = {"name": "Tunde", "age": 16, "grade": "A"}
for key, value in student.items():
    print(f"{key}: {value}")
'''
some usecases
    Reading database records.
    showing user profile details.
    checking configuration settings, etc.
'''

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

# 2. While loop
''' A while loop is used to repeatedy execute a block of code
    as long as a given condition is true. Unlike the for loop
    (which iterates over sequences like lists, tuples, etc.), the
    while loop is condition-based.
'''
#while condition:
    #code block
    #The condition must evaluate to True for the loop to continue running
    #When the condition becomes False, the loop stops


#Using while loop
## Documenting my thoughst##
#Let the loop start with count = 1
#Let it keep printing until count is greater than 5
#Let the loop terminate when the condition is no longer true

##My code
count = 1
while count <= 5:
    print("Number:", count)
    count += 1

#Incrementing with 'while'
num = 1
while num <= 10:
    print(num, end=" ")
    num += 1

#Decrementing with 'while'
timer = 10
while timer > 0:
    print("Countdown:", timer)
    timer -= 1

# While with user input
## keep asking until the user keeps a correct password.
password = ""
while password != "python123":
    password = input("Enter the password: ")
print("Access Granted")

''' Understanding while True
    The while True: loop is an infinite loop - it keeps running 
    unitl you explicitly stop it with a break statement or by 
    exiting the program.
    It is commonly used when;
    -you don't know in advance how many times you want the loop
    to run
    -you want to keep asking the user for input until a valid
    condition is met.
    -you are building continuous programs like menus, login
    systems, or simulations.
'''
#while True:
    # Code  block
    # must include a break statement to stop

# keep asking the user for a name until they type "exit".
while True:
    name = input("Enter your name (type 'exit' to quit): ")
    if name.lower() == "exit":
        print("Goodbye!")
        break 
    print(f"Hello, {name}")

''' Loop Control Statements (break, continue and pass)
    These keywords help us control the behavior of loops (for
    and while). Instead of loops always running all iterations, 
    we can skip steps, stop early, or do noting intentionally.
'''
#1. break
# stops loop immediately. It is used if a condition is met and 
# there's no need to continue looping.
for num in range(1,10):
    if num == 5:
        break 
    print(num)

#The loop stops completely when num ==5.
#Stops searching when an item is found.
#Exit when user input matches a condition.
#Prevent unnecessary iterations.

#2. continue
# skips the current iteration and moves to the next one.
# It is used if you want to ignore some values but keep the
# loop running.
for num in range(1,6):
    if num == 3:
        continue 
    print(num)

#3 is skipped, but the loop continues.

# Some usecases
# skip invalid data.
# ignore unwanted characters (like spaces in a string)
# continue running but avoid certain cases, etc.

#3 Pass
#does nothing. A placeholder to avoid errors. It is used if
#you haven't written the code yet but you want to keep the 
#structure
for num in range(1, 6):
    if num == 3:
        pass    # do nothing for now
    else:
        print(num)

# At num == 3, Python executes pass (nothing happens).

# Some usecases
# Writing code structure (to fill in later).
# placeholders in class/method definitions
# temporarily disable parts of code

#Let's try while True again


#Try and think through this...
while True:
    print("\nMenu:")
    print("1. Say Hello")
    print("2. Say Goodbye")

    choice = input("choose an option: ")

    if choice == "1":
        print("Hello")
    elif choice == "2":
        print("Goodbye")
    elif choice == "3":
        print("Exiting program...")
        break 
    else:
        print("Invalid choice. Try again.")

'''     Menu
        1.  Say Hello
        2.  Say Goodbye
        3.  Exit
'''

# Try and use while True for validation
while True:
    age = input("Enter your age: ")
    if age.isdigit():
        print(f"Your age is {age}")
        break 
    else:
        print("Invalid input. Please enter a number.")

# Lets make a guess
secret = "python"
while True:
    guess = input("Guess the secret word: ")
    if guess.lower() == secret:
        print("Correct! You guess the word.")
        break 
    else:
        print("Wrong! Try again.")
    
#Do you remember this?
balance = 1000
while True:
    print("\nATM Menu:")
    print("1. Check Balance")
    print("2. Withdraw")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        print(f"Your balance is: {balance}")
    elif choice == "2":
        amount = int(input("Enter withdrawal amount: "))
        if amount <= balance:
            balance -= amount 
            print(f"Withdrawal successful. New balance: {balance}")
        else:
            print("Insufficient funds.")
    elif choice == "3":
        print("Thank you for using our ATM. Goodbye!")
        break 
    else:
        print("Invalid option. Try again.")