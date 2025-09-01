# @title 13. Email Slicer(Extract Username from Email)

"""
Overview An Email Slicer is a simple yet useful tool that
extracts the username and domain from an email address.
This project enhances understanding of string manipulation,
user input handling, and string slicing in Python.
This project covers the step-by-step implementation of an
Email Slicer, including handling user input, extracting the
username and domain, and displaying the results.

Key Concepts of Email Slicer in Python

String Manipulation:

- Using string methods like split() and
- Extracting specific parts of a string

User Input Handling:

- Accepting an email address from the user
- Validating the input format

Output Formatting:

- Displaying extracted username and domain clearly
"""

def slicer(email):
    if "@" in email:
        name, domain = email.split("@")
        return f"name is {name}, domain is {domain}"
    else:
        return None
    

mail = input("enter email: ")
print(f"{slicer(mail)}")