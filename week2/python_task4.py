# # # Task 4
# # 1. Your Favorite Life Quote
# # Ask the user to input their favorite quiote.
# # Convert it to title case
# # Print it with quotation marks using escape sequences.
# quote = input("Input your favorite quote: ")
# conv = quote.title()
# print(f"Fav. Quote - \"{conv}\"")

# # 2. Shopping List Manager
# # Create an empty list.
# # Ask the user to enter 3 shopping items (one by one)
# # Add them to the list.
# # Display the list as a single string, separated by commas.
# list = [ ]
# list1 = input("Enter item 1: ")
# list2 = input("Enter item 2: ")
# list3 = input("Enter item 3: ")
# add_list = [list1, list2, list3]
# print(", ".join(add_list))

# # 3. Word Counter
# # Ask the user for a sentence.
# # Split the sentence into a list of words
# # Print how many words are in the sentence.
# sentence = input("Write a sentence: ")
# new2 = sentence.split()
# print(len(new2))

# # 4. Name Organizer
# names = input("Enter 5 names separated by space: ")
# conv = names.lower()
# conv2 = conv.split()
# conv2.sort()
# for name in conv2:
#     print(name)

# 5. Student Score Tracker
name_list = []
score_list = []
student_names = input("Input 3 student names separated by space: ")
new_student_names = student_names.split()
student1 = input(f"Input {new_student_names[0]} score: ")
student2 = input(f"Input {new_student_names[1]} score: ")
student3 = input(f"Input {new_student_names[2]} score: ")
student_score_list = [student1, student2, student3]

print("Student Score Table")
print(f"{new_student_names[0]}\t- {student_score_list[0]}")
print(f"{new_student_names[1]}\t- {student_score_list[1]}")
print(f"{new_student_names[2]}\t- {student_score_list[2]}")



# # 6. Word Analyzer
# word = input("Please input a word: ")
# print("length of word is", len(word))

# print(word.isupper())
# print(word.islower())
# print(word.istitle())
# print(word[::-1])

# # 7. List Manipulation
# cities = ['Lagos', 'Abeokuta', 'Ibadan', 'Ijebu', 'Lekki']
# print(cities)
# city = input("enter 3rd city: ")
# cities[2] = city
# cities.remove("Lekki")
# cities.insert(0, "Iwo")
# print(cities)