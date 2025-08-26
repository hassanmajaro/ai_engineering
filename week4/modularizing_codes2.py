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
                > uv run script.py      # run scripts in the managed environment
        
        Other package managers that you should try exploring

        Method                  Description                         Best for
        pip install ...         Standard installation from PyPi     Most common and simple use case
        pip install -r          Batch install from file             Reproducible projects
         requirments.txt
        virtualenv + pip        Isolated environments               Independent project setups
        conda install ...       Data science ecosystem              Scientific and system-level dependencies
        clone + pip install..   Custom or non-PyPi packages         Local development and experiments
        .whl install            Prebuilt package install            Faster installations
        pip install -e ...      Editable (development) install      Active package development
        uv ...                  All-in-one  modern manager          Speed, simplicity, and full workflow

    
    Creating a Virtual Environment
            What is a Virtual Environment?
            A virtual environment (venv) is an isolated workspace where you can install and manage Python
        packages without affecting the global/system Python installation
            Each project can have its own dependencies, even if they conflict with other projects
            Why should you form the habit of always creating a Venv before starting a project?
                It keeps project dependences seperate
                It prevents version conflicts
                It makes collaboration easier (everyone uses the same environment)
                It is required in many production setups
    
    How to create a Virtual Environment
    # Create a virtual environment
    python -m venv virtual_environment_name
    # This will create a folder inside your working folder with the name "virtual_environment_name"

    to use it, you have to activate it
    1.  Click on the folder
    2.  Look for script and open it
    3.  Look for 'activate'
    4.  Right click on it and look for copy relative path
    5.  Click on it
    6.  Finally to your terminal and select Command prompt then paste the path you copied
        
        alternatively, you can use this script

    > virtual_environment_name\Scripts\activate       # for windows
    > source virtual_environment_name/bin/activate    # linux or macOS

    Deactivating a virtual environment
    > deactivate

    Saving and Sharing Requirements

    # To freeze the installed packages into a file
    > pip freeze > requirements.txt

    # To install them later
    > pip install -r requirements.txt

    Creating Your Own Package

    my_project/
    |
    |-- my_package/                 # Package folder
    |   |-- __init__.py             # Makes this folder a package
    |   |-- math_utils.py           # Module 1
    |   |-- string_utils.py         # Module 2
    |
    |-- main.py                     # Script that use the package
'''

# # **1. init.py
# #   This is a special file that tells python that my_package is a package.
# # It can be empty or used to initialize the package

# # __init__.py
# print("my_package is being imported")

# # Optional: import functions directly for easier access
# from .math_utils import add, subtract
# from .string_utils import capitalize_text

# # **2. math_utils.py
# #   Module for math operations

# # math_utils.py
# def add(a, b):
#     return a + b 

# def subtract(a, b):
#     return a - b

# # **3. String_utils.py
# #   module for string operations

# # string_utils.py
# def capitalize_text(text):
#     return text.capitalize()

# def reverse_text(text):
#     return text[::-1]

# # **4. main.py
# #   using the package

# # main.py

# # Import the whole package
# import my_package

# print(my_package.add(5, 3))                    # 8
# print(my_package.subtract(10, 4))              # 6
# print(my_package.capitalize_text("python"))    # Python

# # OR import specific modules
# from my_package import string_utils

# print(string_utils.reverse_text("hello"))   # olleh

''' 5. Code Reusability
    What is Code Reusability?
        Code reusability means writing code once and using it multiple times instead 
    of rewriting it.
        It helps make programs cleaner, faster to develop, and easier to maintain
        In Python, code reusability is achieved using:
            Functions (reusing blocks of code)
            Modules (saving functions in .py files to import later)
            Packages (organizing modules in folders)
            Classes & Objects (OOP makes reusable blueprings)
            Libraries (built-in or third-party)
    
    Why Reuse Code?
    -   Saves time - no need to rewrite the same logic
    -   Avoids duplication - reduces errors from copy and paste
    -   Improves readability - your code is modular and organized
    -   Easy to maintain - update once, reuse everywhere

    6.  Organizing a Python Project
        A modular project is a way of organizing your code into seperate files and folders,
    each responsible for a specific task.
        This makes the project easier to read, test, and maintain.

    Why use Modular Structure?
    -   Separates concerns - Each file has one responsibility
    -   Easier to debug - You can fix issues in one place without breaking others
    -   Reusability - Functions/modules can be reused in other projects.
    -   Collaboration-friendly - Multiple developers can work on different parts

    Folder & File Structure
    -   Let's say we want to build a Student Records Project
    -   We will first structure our folder and files like this.

    student_project/
    |
    |-- data.py         # handles storing and retrieving student data
    |-- utils.py        # contains helper functions (e.g., calculations, formatting)
    |-- main.py         # entry point to run the project
'''

# # data.py
# students = []

# def add_student(name, track):
#     students.append({"name": name, "track": track})

# def get_students():
#     return students 

# # utils.py
# def format_student(student):
#     return f"{student['name']} is learning {student['track']} at NCC Digital Industrial Innovation Park, Abeokuta."


# # main.py --> Project entry point

# # main.py

# import data 
# import utils 

# # Add some students
# data.add_student("Paul", "AI Engineering")
# data.add_student("Blessing", "AI Development")

# # Print formatted student records
# for s in data.get_students():
#     print(utils.format_student(s))

''' **Let's Try a Bigger Project Structure
    As the project grow, we can organize into folders.

    student_project/
    |
    |-- data/                       # data related fields
    |   |-- __init__.py
    |   |-- data.py
    |
    |-- utils/                      # helper functions
    |   |-- __init__.py
    |   |-- utils.py
    |
    |-- main.py
    |-- requirements.txt

    Lets work on LIbrary Management System
    -   The goal of this project is to 
        -   Manage books in a library
        -   Add books, list books, and borrow books.
        -   Organized into folders and files for modularity

    
    Lets structure the folder and possible files
    library_project/
    |
    |-- data/               # handles storage and retrieval
    |   |-- __init__.py
    |   |-- data.py
    |
    |-- utils/
    |   |-- __init__.py     # helper functions
    |   |-- helpers.py
    |
    |-- services/           # core business logic
    |   |-- __init__.py
    |   |-- library.py
    |
    |-- main.py             # entry point of the program
    |-- requirements.txt    # (optional) external dependencies
'''
