''' Tuple Practice
    Task1: Create and Display
    Ask the user to enter three favorite Nigerian dishes (one at a time)
    Store them in a tuple called dishes
    Print the tuple in a single line, separating items with commas.
    Use the \n escape sequence to print each dish on a new line.
'''
dish1 = input("Input favorite dish: ")
dish2 = input("Input second fav. dish: ")
dish3 = input("Input third fav. dish: ")

dish = (dish1, dish2, dish3)
print("\n".join(dish))

'''`Task2: Tuple and Input
    Ask the user for 5 best friends' names.
    Store them in a tuple friends.
    Print the tupe in reverse order.
'''
friend1 = input("Input best friend name: ")
friend2 = input("Input 2nd best friend name: ")
friend3 = input("Input 3rd best friend name: ")
friend4 = input("Input 4th best friend name: ")
friend5 = input("Input 5th best friend name: ")
friends = (friend1, friend2, friend3, friend4, friend5)
new = list(friends)
new.reverse()
print(new)

'''# Task3: Tuple Operations
    Create a tuple of 5 Nigerian states entered by the user.
    Printe the first state and last state.
    Check if "Lagos" is in the tuple and print "Yes" or "No".
    Print the number of states entered.
'''
state1 = input("Enter a state: ")
state2 = input("Enter 2nd state: ")
state3 = input("Enter 3rd state: ")
state4 = input("Enter 4th state: ")
state5 = input("Enter 5th state: ")
state = (state1, state2, state3, state4, state5)
print(f"first state is {state[0]}, and last state is {state[4]}")
print("Lagos" in state)
print("no of state entered is", len(state))

''' Task4: Tuple Unpacking
    Ask a user for their;
    first name, age, favorite color, home town
    store them in a tuple profile and unpack into variables
    print and use escape sequence to align each piece of information nicely
'''
first_name = input("What is your first name? ")
age = int(input("What is your age? "))
fav_color = input("What is your favorite color? ")
home_town = input("What is your home town? ")

profile = (first_name, age, fav_color, home_town)
first_name, age, fav_color, home_town = profile
print(f"Name:\t\t{first_name}\nAge:\t\t{age}\nFav. Color:\t{fav_color}\nHome Town:\t{home_town}")

''' Task5: Modify Tuple Indirectly
    Ask a user to enter three items for their shoppingn list
    store in a tuple shopping_list
    convert it into a list, then ask for more items to add.
    convert back to a tuple and print the updated list using join() to display items separated by "|"
'''
shop1 = input("Enter shopping item1: ")
shop2 = input("Enter shopping item2: ")
shop3 = input("Enter shopping item3: ")
shopping_list = (shop1, shop2, shop3)
conv_list = list(shopping_list)

add_item = input("Add one more item: ")
add_item2 = input("Add another item: ")

conv_list.append(add_item)
conv_list.append(add_item2)
conv2 = tuple(conv_list)
print(" | ".join(conv2))

'''Task6: Attendance Tracker
    Write a Python program that;
    Stores the days of the week in a tuple.
    Stores the months of the year in another tuple.
    Asks the user to enter: student's name, gender, course track, current month number(1-12), current day number(1-7) and print
'''
days_of_the_week = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")
months_of_the_year = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
name = input("Enter Student Name: ")
age = input("Enter Gender: ")
course = input("Enter Course Track: ")
month = int(input("Enter Current Month in number(1-12): ")) - 1
day = int(input("Enter Current Day in number(1-7): ")) - 1

print("Days of the week", days_of_the_week)
print("Months of the year", months_of_the_year)
print(f'''
    Student Name:   {name}
    Student Age:    {age}
    Course Track:   {course}
    Current Month:  {months_of_the_year[month]}
    Current Day:    {days_of_the_week[day]}
''')