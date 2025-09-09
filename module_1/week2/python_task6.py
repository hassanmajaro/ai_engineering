# ''' Task1: Fruit Collector
#     Ask the user to enter 5 favorite fruits. Store them in a set and display the set.
# '''
# fruit1 = input("Enter favorite fruit: ")
# fruit2 = input("Enter 2nd favorite fruit: ")
# fruit3 = input("Enter 3rd favorite fruit: ")
# fruit4 = input("Enter 4th favorite fruit: ")
# fruit5 = input("Enter 5th favorite fruit: ")
# fav_fruits = set([fruit1, fruit2, fruit3, fruit4, fruit5])
# print(fav_fruits)

# ''' Task2: Unique Name Collector
#     Write a program that collects the names of people attending a seminar (no duplicates allowed) and displays them in alphabetical order
# '''
# people = input("Enter the name of people attending a seminar (separated by comma): ")

# # name_of_people = people.split()
# attendance = set(people.split(','))
# sorting = sorted(attendance)
# print(sorting)

# ''' Task3: Simulate a football match ticket system
#     Store all seat numbers (1 to 50) in a set.
#     Ask users to "book" a seat by entering the number.
#     Remove booked seats from the set.
#     Show remaining seats after each booking.
# '''
# seat_numbers = set(range(1, 51))
# book = int(input("book a seat (1-50): "))
# seat_numbers.remove(book)
# print("Remaining seats are;", seat_numbers)

# ''' Task4: Create a Unique Voters Registration System
#     Ask for voter names and store in a set.
#     If a voter tries to register twice, display a warning.
#     After registration, display the total number of unique voters.
# '''
# voters = set()
# voter1 = input("Input voter name: ")
# voter2 = input("Input 2nd voters name: ")
# voter3 = input("Input 3rd voters name: ")
# voters.add(voter1)
# voters.add(voter2)
# voters.add(voter3)

# for voter in voters:
#     print("Warning!") 
# print("Total number of voters are", len(voters))