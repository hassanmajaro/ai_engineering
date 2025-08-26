''' **Modularizing Your Code 2
    3.  Python Modules
            What a module is (a .py that can be reused)
            Importing built-in modules (math, random, datetime)
            Writing your own module (creating my_module.py and importing it)
            Aliasing modules (import numpy as np)
    
    What is a Module?
        A module in Python is simply a file .py extension that contains
    Python code (functions, variables, or classes) which can be reused in
    other programs.
        Instead of writing the same code again and again, you can write it
    once in a module and then import it anywhere.
        Let's think of a module as a toolbox. Each tool (function, variable,
    or class) can be taken out and used whenever needed, without rebuilding
    the tool from scratch.

    Importing Built-in Modules
        Python already comes with m any pre-built modules that you can use
    directly.
        Some common examples are:
            math - for mathematical operations
            random - for generating random numbers
            datetime - for working with dates and time. etc.
        To use built-in modules, you have to load them into your environment,
    that is, import them
'''

# # Different Ways to Import Modules
# #1. Import the whole module
# import math 

# # Let's put it to use
# print(math.sqrt(9))
# # NB: You must specify the module when calling a function within it

# #2. Import as an alias
# import math as m

# # lets put it to use

# print(m.sqrt(25))   # - this shortens the module name, this is common with libraries like numpy, pandas, etc

# #3. Import specific functions or variables
# from math import sqrt, pi 

# print(sqrt(36))
# print(pi)
# # - here you don't need the prefix 'math.' anymore

# #4. Import everyhing from the  module
# from math import *

# print(sqrt(49))
# print(pi)
# # - This is actually not recommended because it can cause conflicts if two modules have functions with the same name


''' **Writing Your Own Module**
        step1: create a folder. name it my_module
        step2: create a file inside the folder. name it first.py
        step3: create another file inside the same folder. name it second.py
        step4: create another file inside the same folder. name it main.py

        here is the folder structure
            project_folder/
            |
            |-- my_module/
            |   |-- first.py
            |   |-- second.py
            |   |-- main.py
        Note that anyonw with forward slacsh is a folder while the ones with
        extensions are the files.
'''
# # my_modules/first.py
# def add(a, b):
#     return a + b 

# def subtract(a, b):
#     return a - b 

# def multiply(a, b):
#     return a * b 

# def divide(a, b):
#     if b != 0:
#         return a / b 
#     else:
#         return "Cannot divide by zero"

# # my_modules/second.py
# def greet(name):
#     return f"Hello, {name}! I am creating my own module"

# def reverse_string(string):
#     return string[::-1]

# def count_characters(string):
#     return len(string)

# def count_words(string):
#     return len(string.split())

# # my_modules/main.py
# import first 
# import second 

# # let's use the function in the first.py file
# print("===Math Functions===")
# print("5 + 3 =", first.add(5,3))
# print("10 - 4 =", first.subtract(10,4))
# print("6 * 7 =", first.multiply(6, 7))
# print("20 / 5 =", first.divide(20, 5))

# # lets use the functions in the second.py file
# print("\n===String Functions===")
# print(second.greet("Ridwan"))
# print("Reverse of 'Python' =", second.reverse_string("Python"))
# print("Character count in sentence =", second.count_characters("Python modules are powerful"))
# print("Word count in sentence =", second.count_words("Python modules are powerful"))


''' 4.  Python Packages
            What a package is (a folder wit init.py)
            Installing and using third-party packages (pip install requests, import requests)
            Organizing multiple modules into a package
        
        What is a Package?
            A package in python is a way to organize related modules together into a folder
            Inside this folder, there must be a special file called __init__.py (can be empty).
        This file tells Python that the folder should be treated as a package.
            Think of package as a standard mechanic workshop, and each module is a different 
        toolbox inside the workshop. The init.py file is like the label on the workshop telling
        passerys that this is a mechanic workshop.
    
        Third-Party Packages
            Python comes with some built-in modules, but you also install
        extra packages created by others.

        These packages are stored in the Python Package Index (PyPI)

        We install them using pip (Python's package manager) or conda a

        How to Install Python Packages
        1.  using pip
                This is the most common method
                It installs packages from PyPI. It is the Python's central package
            repository.
                To work with it. You are to use it in your terminal

                    > pip install requests                    # Install latest version
                    > pip install requests==2.28              # Install specific version
                    > pip install --upgrade requests          # upgrade existing package
                    > pip uninstall requests                  # remove package

        
        2.  To use uv
                #run this command on your terminal depending on your OS
                #recommended method: standalone installer
                    #macOS/Linux
                > curl -LsSf https://astral.sh/uv/install.sh  | sh

                #or

                    # Windows
                > powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

                after installation, verify version
                > uv --version
                    using uv to install packages
                    but before it works you must have a working virtual environment
                
                > uv add requests       # install package and update project files
                > uv pip install flask  # works like pip but much faster
                > uv remove requests    # uninstall
                > uv venv               # create a virtual environment automatically
'''