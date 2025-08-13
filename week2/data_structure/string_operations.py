# # Upper ()
# # Converts all characters in the string to uppercase
# name = "Ada Balogun"
# print(name.upper())         # Output: ADA BALOGUN

# # lower()
# # Converts all characters in the string to lowercase
# name = "ADA BALOGUN"
# print(name.lower())     # Output: ada balogun

# # title()
# # converts all words in the strict to title case
# sentence = "python is amazing"
# print(sentence.title())    # Output: Python Is Amazing

# # strip()
# # removes whitespace for (or specified characters) from both ends of the string
# text = "    Abuja   "
# print(text.strip())        # Output: Abuja

# # replace()
# # replaces occurences of a substring with another substring
# message = "I love Java"
# print(message.replace("Java", "Python"))        # Output: I love Python

# # swapcase()
# # switches lowercase to uppercase and vice versa.
# text = "Hello ABEOKUTA"
# print(text.swapcase())          # Output: hELLO abeokuta

# # lstrip()
# # removes whitespace (or specified characters) from the left side only
# text = "    Nigeria"
# print(text.lstrip())            # Output: Nigera

# # rstrip()
# # removes whitespace (or specified characters) from the right side only
# text = "Nigera  "
# print(text.rstrip())            # Output: Nigeria

# # split()
# # splits a string into a list using a separator (defualt is space)
# fruits = "mango orange banana"
# print(fruits.split())           # Output: ['mango', 'orange', 'banana']

# # rsplit()
# # splits a string into a list from the right side
# text = "one,two,three,four"
# print(text.rsplit(",", 2))       # Output: ['one,two', 'three', 'four']

# # splitlines()
# # splits a string into a list at each newline(\n)
# lines = "Line 1\nLine 2\nLine 3"
# print(lines.splitlines())       # Output: ['Line 1', 'Line 2', 'Line 3']

# # join()
# # joins a list of strings into one string with a specified separator
# words = ["I", "love", "Python"]
# print(" ".join(words))          # Output: I love Python

# # center()
# # centers the string within a specified width, padding with spaces or characters.
# text = "Python"
# print(text.center(20, "-"))     # Ouput: -------Python-------

# # ljust()
# # left-aligns the string within a specified width, padding with spaces or characters.
# text = "Python"
# print(text.ljust(10, "*"))      # Output: Python*****

# # rjust()
# # right-aligns the string within a specified width, padding with spaces or characters.
# text = "Python"
# print(text.rjust(10, "*"))      # Output: ****Python

# zfill()
# pads a numeric string on the left with zeros until it reaches a given length
num = "42"
print(num.zfill(5))             # Output: 00042

# isalpha()
# checks if the string contains only letters
print("Lagos".isalpha())        # True
print("Lagos123".isalpha())     # False

# isdigit()
# checks if the string contains only digits
print("12345".isdigit())        # True
print("123a".isdigit())         # False

# isalnum()
# checks if the string contains only letters and digits
print("Python3".isalnum())      # True
print("Python 3".isalnum())     # False