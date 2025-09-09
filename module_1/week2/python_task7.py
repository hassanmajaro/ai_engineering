''' Task1: Student Bio Data Storage
    Create a program that collects student bio-data from user input (name, age, gender, courses) and stores it in a dictionary
        Courses should be stored as a list
        Display the bio-data neatly using escape sequences.
    Requirements:
        use input() to collect details
        use dictionary operations (dict[key] = value) to store data.
        use print() formatting with \n and \t for better output.
'''
name = input("Name: ")
age = int(input("Age: "))
gender = input("Gender: ")
courses = input("Courses: ")

student = {
    "name": name,
    "age": age,
    "gender": gender,
    "courses": [courses]
}
print("\nStudent Bio-Data")
print(f"Name: \t\t{student["name"]}\nAge: \t\t{student["age"]}\nGender: \t{student["gender"]}\nCourses: \t{student["courses"]}")

''' Task2: Super Market Price List
    Create a program that stores items and their prices in a dictionary
        items should come from a list.
        prices are entered by the user
        display all items and prices, then allow the user to update the price of an item.
    Requirements:
        use dictionary update method .update() or assignment.
        use .keys() to display available items
        use input validation (no advanced functions)
'''
items = ["monitor", "keyboard", "mouse", "system unit"]
item1_price = float(input("Monitor price: "))
item2_price = float(input("Keyboard price: "))
item3_price = float(input("Mouse price: "))
item4_price = float(input("System unit price: "))

store_items = {
    items[0]: (f"${item1_price}"),
    items[1]: (f"${item2_price}"),
    items[2]: (f"${item3_price}"),
    items[3]: (f"${item4_price}")
}
print(f"Store Item and prices are: {store_items}")

update_item = float(input(f"Update {items[2]} price: $"))
store_items.update({items[2] : update_item})

print(f"Available items are; {store_items.keys()}")

''' Task3: Days and Activities Pairing
    Stores days of the week in a tuple and ask the user to input an activity for three specific days.
        Use dictionary comprehension to pair days and activities
        Print the dictionary
    Requirements:
        use tuple for days
        use {day: activity for day, activity in zip(...., ....)}.
    Tip: Research on how to use zip()
'''
days = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")
day1_activity = input(f"Input activity for {days[0]}: ")
day2_activity = input(f"Input activity for {days[1]}: ")
day3_activity = input(f"Input activity for {days[2]}: ")
day4_activity = input(f"Input activity for {days[3]}: ")
day5_activity = input(f"Input activity for {days[4]}: ")
day6_activity = input(f"Input activity for {days[5]}: ")
day7_activity = input(f"Input activity for {days[6]}: ")

activity = [day1_activity, day2_activity, day3_activity, day4_activity, day5_activity, day6_activity, day7_activity]
print(dict(zip(days, activity)))

''' Task4: Unique Members Registration
    Ask the user to enter three names separated by commas
        convert them to a set to ensure uniqueness
        create a dictionary where each name is a key and its length is the value.
    Requirements:
        use .split(",") and set() to remove duplicates.
        use dictionary comprehension {name: len(name) for name in set_of_names}
'''
names = input("Enter three names (separated by comma): ")
set_names = set(names.split(","))
dict_names = {name: len(name) for name in set_names}
print(dict_names)

''' Task5: Contact Quick Lookup
    Store three names and their phone numbers in two separate tuples
        Create a dictionary from the using dict(zip(....)).
        Ask the user for a name and display the corresponding number (or an error message).
    Requirements:
        use zip() and dict() to combine tuples
        use .get() for safe retrieval
        no loops.
'''
names = ("Oba", "Ope", "David")
phone_numbers = ("23470", "23480", "23490")

details = {name: num for name, num in zip(names, phone_numbers)}
user = input("Enter name: ")
print(f"User\'s number is",details.get(user))