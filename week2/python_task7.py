''' Task1: Student Bio Data Storage
    Create a program that collects student bio-data from user input (name, age, gender, courses) and stores it in a dictionary
        Courses should be stored as a list
        Display the bio-data neatly using escape sequences.
    Requirements:
        use input() to collect details
        use dictionary operations (dict[key] = value) to store data.
        use print() formatting with \n and \t for better output.
'''

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

''' Task3: Days and Activities Pairing
    Stores days of the week in a tuple and ask the user to input an activity for three specific days.
        Use dictionary comprehension to pair days and activities
        Print the dictionary
    Requirements:
        use tuple for days
        use {day: activity for day, activity in zip(...., ....)}.
    Tip: Research on how to use zip()
'''

''' Task4: Unique Members Registration
    Ask the user to enter three names separated by commas
        convert them to a set to ensure uniqueness
        create a dictionary where each name is a key and its length is the value.
    Requirements:
        use .split(",") and set() to remove duplicates.
        use dictionary comprehension {name: len(name) for name in set_of_names}
'''

''' Task5: Contact Quick Lookup
    Store three names and their phone numbers in two separate tuples
        Create a dictionary from the using dict(zip(....)).
        Ask the user for a name and display the corresponding number (or an error message).
    Requirements:
        use zip() and dict() to combine tuples
        use .get() for safe retrieval
        no loops.
'''