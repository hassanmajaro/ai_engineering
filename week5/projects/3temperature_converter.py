"""
A temperature converter is a simple yet essential
application that allows users to convert temperatures
between different units, such as Celsius, Fahrenheit, and
Kelvin. This project enhances understanding of
mathematical operations, conditional statements, and user
input handling in Python.
This covers the step-by-step implementation of a
temperature converter, user input handling, mathematical
conversions, and function-based design.

Key Concepts of Temperature Converter in Python

Mathematical Conversion Formulas:
- Celsius to Fahrenheit: (C × 9/5) + 32
- Fahrenheit to Celsius: (F - 32) × 5/9
- Celsius to Kelvin: C + 273.15
- Kelvin to Celsius: K - 273.15
- Fahrenheit to Kelvin: (F - 32) × 5/9 + 273.15
- Kelvin to Fahrenheit: (K - 273.15) × 9/5 + 32

User Input Handling:

Using input() function
Handling invalid inputs
"""

def cel_fah(C):
    return f"{C} degree Celcius to Fahrenheit is {((C * 9/5) + 32):.2f}"

def fah_cel(F):
    return f"{F} degree Fahrenheit to Celcius is {((F - 32) * 5/9):.2f}"

def cel_kel(C):
    return f"{C} degree Celcius to Kelvin is {(C + 273.15):.2f}"

def kel_cel(K):
    return f"{K} degree Kelvin to Celcius is {((K - 273.15)):.2f}"

def fah_kel(F):
    return f"{F} degree Fahrenheit to Kelvin is {((F - 32) * 5/9 + 273.15):.2f}"

def kel_fah(K):
    return f"{K} degree Kelvin to Fahrenheit is {((K - 273.15) * 9/5 + 32):.2f}"


while True:
    print("\nTemperature Converter")
    print("1. Celcius to Fahrenheit")
    print("2. Fahrenheit to Celcius")
    print("3. Celcius to Kelvin")
    print("4. Kelvin to Celcius")
    print("5. Fahrenheit to Kelvin")
    print("6. Kelvin to Fahrenheit")

    try:
        choice = int(input("\nEnter 1-6 for converter or 00 to exit: "))

        if choice == 1:
            print("You choose conversion from Celcius to Fahrenheit")
            conv1 = float(input("Enter temperature to convert: "))
            print("calculating.....")
            print(cel_fah(conv1))

        elif choice == 2:
            print("You choose conversion from Fahrenheit to Celcius")
            conv1 = float(input("Enter temperature to convert: "))
            print("calculating.....")
            print(fah_cel(conv1))

        elif choice == 3:
            print("You choose conversion from Celcius to Kelvin")
            conv1 = float(input("Enter temperature to convert: "))
            print("calculating.....")
            print(cel_kel(conv1))

        elif choice == 4:
            print("You choose conversion from Kelvin to Celcius")
            conv1 = float(input("Enter temperature to convert: "))
            print("calculating.....")
            print(kel_cel(conv1))

        elif choice == 5:
            print("You choose conversion from Fahrenheit to Kelvin")
            conv1 = float(input("Enter temperature to convert: "))
            print("calculating.....")
            print(fah_kel(conv1))

        elif choice == 6:
            print("You choose conversion from Kelvin to Fahrenheit")
            conv1 = float(input("Enter temperature to convert: "))
            print("calculating.....")
            print(kel_fah(conv1))

        elif choice == 00:
            print("Exiting.... Thank you!")
            break 

    except ValueError as ve:
        print("Error", ve)