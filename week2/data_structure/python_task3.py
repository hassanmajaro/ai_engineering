# Task 1
# 1 Write a program to take a string input from the user and display it in uppercase
name = input("Enter full name? ")

print (f"The name of this user is {name.upper()}")



# 2 Given the string "Python", print its first and last characters
text = "Python"
print(text[0])
print(text[-1])



# 3 Ask the user for their name and print "Hello, !" where is the user input
name = input("Enter name: ")
print(f"\"Hello {name}!\"")



# 4 Write a program to count the number of characters in a string without using len()
word = "How many words are here?"
print(word.index("?") + 1)



# 5 Given "Hello World", replace "World" with "Python"
given_word = "Hello World"
print(given_word.replace("World", "Python"))




# Task 2
# 6. Check if a given string contains substing "python" (case-insensitive).
word = "Is python a lot?"
print("python" in word)



# 7 Write a program to reverse a string without using slicing (::-1)
word = "Python"
print("".join(reversed(word)))



# 8 Given a string with extra spaces, remove the leading and trailing spaces
name = "  Hassan  "
print(name.strip())



# 9 Ask the user to enter a sentence and print the number of vowels in it
sen = input("Input sentence: ")
print(sen.count("a") + sen.count("e") + sen.count("i") + sen.count("o") + sen.count("u"))



# 10 Convert a string "1234" to an integer and multiple it by 2
string = "1234"
conv = int(string) * 2
print (conv)




# Task 3
# Pattern Matching & Splitting
# 11 Given "apple,banana,orange", split the string into a list of fruits
text = "apple,banana,orange"
print("List of fruits:", text.split(","))



# 12 Ask the user for a sentence and print each word on a new line
sentence = input("Input sentence: ")
words = sentence.split(" ")
print("\n".join(words))



# 13 Replace all spaces in a string with underscores(_)
string = "this is python programming language"
print(string.replace(" ", "_"))



# 14 Count how many times the letter "a" appears in Banana
fruit = "Banana"
print(fruit.count("a"))



# Check if a given string starts with https://
link = "https://google.com"
print(link.startswith("https://"))