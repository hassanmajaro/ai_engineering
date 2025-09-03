# ''' Modularizing Your Codes 3 (Object Oriented Programming)
#     Table of contents
#     - Introduction to classes
#     - why classes are important
#     - basic class structure
#     - objects and instances
#     - understanding self
#     - attributes
#     - methods
#     - other important methods
#     - simple examples
#     - intermediate examples
#     - complex examples
#     - best practices

#     What is a Class?
#     A class is like a blueprint or template that defines what
#     something should look like and what it can do. Think of it
#     as a meat pie cutter - it defines the shape and characteristics,
#     but it's not the actual meat pie itself.
#     -   take a look at this;
#         - a house blueprint shows where rooms go, but it's not
#         a house you can live in.
#         - a car design document describes features, but you can't
#         drive the design.
#         - a recipe tells you how to make a cake, but the recipe is
#         not edible

#     Object/Instance
#     What is an Object/Instance?
#     An object (also called an instance) is a specific, real item
#     created from a class blueprint. It's the acutal "thing" you 
#     can use and interact with.
#     -   take a look at this;
#         - you actual house built from the blueprint
#         - a specific toyota camry manufactured from car designs
#         - the delicious cake baked from the recipe

#     Key Characteristics of Classes
#     - Encapsulation: groups related data and functions together
#     - Abstraction: hides complex implementation details
#     - Inheritance: can create new classes based on existing ones
#     (reusability- write once, use many times)

#     Why classes are important
#     -   classes help us:
#         - organize code: keep related data and functions together
#         - model real world: represent real-world entities in code
#         - reduce repetition: avoid writing the same code multiple times
#         - maintain code: easier to update and fix bugs
#         - scale applications: build larger, more complex programs

#     The Foundation
#     -   __init__ and self
#         - before we dive into attributes and methods, we need to
#         understand two special concepts that make everything work:
#         init and self

#     What is init?
#     __init__ is a special method (called a constructor) that
#     automatically runs when you create a new object. Think of it
#     as the "birth certificate" process - it sets up all the basic
#     information about the new object.

#     Real-World Analogy
#     -   when a baby is born in Nigeria, certain things happen 
#     automatically:
#         - birth certificate is created
#         - name is assigned
#         - parents are recorded
#         - date of birth is noted
#     -   similarly, when an object is "born" (created), __init__
#     automatically:
#         - sets up the object's attributes
#         - assigns initial values
#         - prepares the object for use
# '''

# # class Student:
# #     def __init__(self, name, course, level): # this runs automatically
# #         print("Creating a new student...")
# #         self.name = name 
# #         self.course = course 
# #         self.level = level 
# #         print(f"Student {name} has been created!")

# # # when you create a student, __init__ runs automatically
# # kemi = Student("Kemi Adebayo", "Computer Science", 300)

# ''' What is Self? Self is a reference to the specific object
#     you're working with. It's like saying "this particular student"
#     or "this specific bank account."

#     Real-world Analogy
#     -   In a classroom with many students:
#         -   when the teacher says "Kemi, what is your course?" - "your"
#         refers to Kemi specifically
#         -   when the teacher says "Chinedu, what is your level?" - "your"
#         refers to Chinedu specifically

#     -   In programming:
#         -   self.name means "this specific objet's name"
#         -   self.course means "this specific object's course"

#     Visual Illustration
#     Class: Student (The Template)
#     |-- def __init__(self, name, course):
#     |   |-- self.name = name        <-- "give THIS object a name"
#     |   |-- self.course = course    <-- "give THIS oject a course"

#     Creating Objects:
#     |-- kemi = Student("Kemi", "CS")
#     |   |-- self refers to Kemi <-- kemi.name = "Kemi"
#     |-- chinedu = Student("Chinedu", "Engineering")
#     |   |-- self refers to chinedu --> chinedu.name = "Chinedu"
#     |-- Fatima = Student("Fatima", "Medicine")
#         |-- self refers to fatima --> fatima.name = "Fatima"
# '''

# # How init and self Work Together
# class NigerianStudent:
#     def __init__(self, name, state, course):
#         print(f"Step 1: Creating student object...")
#         self.name = name            # Step 2: assign name to THIS object
#         self.state_of_origin = state    # Step 3: assign state to THIS object
#         self.course = course        # Step 4: assign course to THIS object
#         self.student_id = self.generate_id()    # Step 4: Generate ID for THIS object
#         print(f"Step 6: {self.name} from {self.state_of_origin} is ready!")

#     def generate_id(self):
#         import random 
#         return f"UNISAIL {random.randint(1000, 9999)}"
    
# # when you create an object, here's what happens:
# ayo = NigerianStudent("Ayo Daniel", "Lagos", "Street Statistics")
# print(ayo.name)
# print(ayo.student_id)


# # more example
# class PhoneUser:
#     def __init__(self, name, network):
#         self.name = name 
#         self.network = network 
#         self.airtime = 0 
#         print(f"{self.name} joined {self.network} network")

#     def buy_airtime(self, amount):
#         self.airtime += amount      # self ensures it goes to the RIGHT person
#         return f"{self.name} now has N{self.airtime} airtime"
    
# # creating multiple users
# abeeb = PhoneUser("Abeeb Bakare", "MTN")
# onisemo = PhoneUser("Onisemo Williams", "Airtel")

# ''' Key rules
#     1.  init always taks self as first parameter
#     2.  all methods take self as first parameter
#     3.  never pass self manually when calling methods
#     4.  use self inside methods to access object's attributes
#     5.  self refers to the specific object being use


#     Attributes
#     What are Attributes? Attributes are the characteristics,
#     properties, or data that describe an object. They answer the
#     question "What does this object look like?" or "what information
#     does this object store?"

#     Real-world analogy
#     -   think of a Nigerian National ID card
#         -   me: "Adebayo Tosin"
#         -   age: 28
#         -   state of origin: "Lagos"
#         -   LGA: "ikeja"
#         -   Occupation: "Software Developer"
#     these are all attributes - they describe WHO the person is,
#     not what they can DO    
# '''
# # defining attributes of a student
# class Student:
#     def __init__(self, name, course, level, state_of_origin):
#         self.name = name 
#         self.course = course 
#         self.level = level 
#         self.state_of_origin = state_of_origin 
#         self.cgpa = 0.0

# # creating a student object
# Fathia = Student("Fathia Abdul", "Biochemistry", 300, "Ogun State")

# # accessing attributes
# print(Fathia.name)
# print(Fathia.course)
# print(Fathia.state_of_origin)

# '''Types of Attributes
# 1.  Instance attributes - unique to each object
# '''
# student1 = Student("Anthony Johnson", "Engineering", 200, "Ogun")
# student2 = Student("Fadilat Hassan", "Medicine", 400, "Lagos")

# print(student1.name)
# print(student2.name)

# '''2. Class Attributes - shared by all objects of the dress'''
# class Student:
#     university = "Federal University of Technology Akure"

#     def __init__(self, name, course):
#         self.name = name 
#         self.course = course 

# print(Student.university)
# print(student1.university)
# print(student2.university)

# ''' Methods: The Actions (What Objects CAN DO)
#     What are Methods?
#     Methods are functions that belong to a class. They define
#     what actions an object can perform. They answer the question
#     "What can this object do?"

#     Real-World Analogy
#     -   Think of what a Nigeriann student do
#         - Study()
#         - WriteExam()
#         - PaySchoolFees()
#         - RegisterCourses()
#         - AttendLectures()
#     These are all methods - they describe what the person can DO,
#     not what they look like
# '''
# class Student:
#     def __init__(self, name, course, level):
#         # Attributes
#         self.name = name 
#         self.course = course 
#         self.level = level 
#         self.cgpa = 0.0 
#         self.fees_paid = False 

#     # Method: action the student can do
#     def pay_school_fees(self):
#         self.fees_paid = True 
#         return f"{self.name} has paid school fees for {self.level} level"
    
#     # Method: another action
#     def register_courses(self):
#         if self.fees_paid:
#             return f"{self.name} has registered courses for {self.course}"
#         else:
#             return f"{self.name} must pay school fees first!"
        
#     # Method: Calculates CGPA
#     def calculate_cgpa(self, grades):
#         if grades:
#             self.cgpa = sum(grades) / len(grades)
#             return f"{self.name}'s CGPA is now {self.cgpa:.2f}"
#         return "No grades provided"
    
# # using methods
# Abiodun = Student("Abiodun Akinola", "Gistology", 600)
# print(Abiodun.pay_school_fees())
# print(Abiodun.register_courses())
# print(Abiodun.calculate_cgpa([4.2, 3.8, 4.0, 3.5]))

# ''' Types of Methods
#     1.  Instance Methods - work with specific object data
# '''
# def pay_school_fees(self):
#     return f"{self.name} has paid school fees"

# ''' 2.  Class Methods - work with class-level data'''
# @classmethod 
# def get_university(cls):
#     return cls.university

# ''' 3.  Static Methods - don't need object or class data'''
# @staticmethod 
# def academic_calendar():
#     return "Academic session runs from September to July"

# ''' How Attributes and Methods Work Together
#     The Relationship
#     -   attributes store the data
#     -   Methods use and modify that data
# '''

# class BankAccount:
#     def __init__(self, owner, bank_name, balance=0):
#         # ATTRIBUTES - What the account HAS
#         self.owner = owner 
#         self.bank_name = bank_name 
#         self.balance = balance 
#         self.account_number = self.generate_account_number()

#         # METHODS - What the account can DO
#     def deposit(self, amount):
#         """Add money to the account"""
#         if amount > 0:
#             self.balance += amount  # Method changes attribute
#             return f"N{amount:,} deposited to {self.owner}'s {self.bank_name} account. New balance: N{self.balance:,}"
#         return "Invalid deposit"
        
#     def withdraw(self, amount):
#         """Remove money from the account"""
#         if amount > 0 and amount <= self.balance:
#             self.balance -= amount  # method changes attribute
#             return f"N{amount:,} withdrawn from {self.owner}'s account. New balance: N{self.balance:,}"
#         return "Insufficient funds or invalid amount"

#     def transfer(self, amount, recipient):
#         """Transfer money to another account"""
#         if amount > 0 and amount <= self.balance:
#             self.balance -= amount 
#             return f"N{amount:,} transferred from {self.owner} to {recipient}. Remaining balance: N{self.balance:,}"
#         return "Transfer failed: Insufficient funds"
    
#     def check_balance(self):
#         """Check current balance"""
#         return f"{self.owner}'s {self.bank_name} account balance: N{self.balance:,}"
    
#     def generate_account_number(self):
#         """Generate a unique account number"""
#         import random 
#         return f"01{random.randint(10000000, 99999999)}"
    
# # creating and using the account
# adunni_account = BankAccount("Adunni Olaleye", "AXT Bank", 5000)

# # Attributes (characteristics)
# print(f"Owner: {adunni_account.owner}")
# print(f"Bank: {adunni_account.bank_name}")
# print(f"Account Number: {adunni_account.account_number}")

# # Methods (actions)
# print(adunni_account.deposit(25000))
# print(adunni_account.withdraw(10000))
# print(adunni_account.transfer(15000, "Sunday James"))
# print(adunni_account.check_balance())

# ''' Visual Representation

#     CLASS: Danfo Bus
#     ├── ATTRIBUTES (What it HAS)
#     │   ├── route = "Garage to Ogolonto"
#     │   ├── conductor_name = "Juwon"
#     │   ├── capacity = 4
#     │   ├── current_passengers = 0
#     │   └── fare = 200
#     │
#     └── METHODS (What it can DO)
#         ├── pick_passenger() → current_passengers increases
#         ├── drop_passenger() → current_passengers decreases
#         ├── collect_fare() → "Pay your ₦200!"
#         ├── announce_bus_stop() → "Next stop: Ebute!"
#         └── honk() → "Pam pam pam!"

#     OBJECT: my_danfo
#     ├── Uses the attributes with specific values
#     └── Can perform all the methods

#     Attributes vs Methods 

#     | Attributes                | Methods                       |
#     |----------------           |-------------                  |
#     | Store data/information    | Perform actions               |
#     | Answer "What is it?"      | Answer "What can it do?"      |
#     | Nouns (name, course, state) | Verbs (study, pay, register)|
#     | Hold values               | Execute code                  |
#     | Can be read/changed       | Can be called/executed        |
#     | `student.name`            | `student.pay_fees()`          |
# '''

# # Practise Exercise 1
# # given this class, identify the attributes and methods
# class NaijaPhone:
#     def __init__(self, brand, model, network_provider):
#         self.brand = brand 
#         self.model = model 
#         self.network_provider = network_provider 
#         self.airtime_balance = 0
#         self.data_balance = 0
#         self.is_on = False 

#     def power_on(self):
#         self.is_on = True 
#         return f"{self.brand} phone is now on. Network: {self.network_provider}"
    
#     def buy_airtime(self, amount):
#         self.airtime_balance += amount 
#         return f"N{amount} airtime purchased. Balance: N{self.airtime_balance}"
    
#     def make_call(self, number):
#         if self.is_on and self.airtime_balance > 0:
#             self.airtime_balance -= 10
#             return f"Calling {number}... Remaining airtime: N{self.airtime_balance}"
#         return "Cannot make call. Check phone power and airtime balance"
    
#     def send_sms(self, message, number):
#         if self.airtime_balance >= 4:
#             self.airtime_balance -= 4
#             return f"SMS sent to {number}: '{message}'. Remaining airtime: N{self.airtime_balance}"
#         return "Insufficient airtime to send SMS"
    

# # Practice Exercise2
# # given this class, identify the attributes and methods
# class BTRBus:
#     def __init__(self, route, bus_number):
#         self.route = route 
#         self.bus_number = bus_number 
#         self.current_stop = "Ikorodu"
#         self.passenger_count = 0
#         self.fare = 300

#     def announce_stop(self):
#         return f"Next stop: {self.current_stop}. Fare is N{self.fare}"
    
#     def board_passengers(self, count):
#         self.passenger_count += count 
#         return f"{count} passengers boarded. Total: {self.passenger_count}"
    

# # Practice Exercise 3
# # given this class, identify the attributes and methods
# class MarketTrader:
#     def __init__(self, name, market_name, goods):
#         self.name = name 
#         self.market_name = market_name 
#         self.goods = goods 
#         self.daily_sales = 0

#     def advertise_goods(self):
#         return f"{self.name} at {self.market_name}: Fresh {', '.join(self.goods)} available!"
    
#     def make_sale(self, amount):
#         self.daily_sales += amount 
#         return f"Sale made! Today's total: N{self.daily_sales:,}"
    

# ''' Encapsulation
#     What is Encapsulation?
#     Encapsulation is like putting related items in a box and controlling 
#     who can access them. It groups related data (attributes) and functions (methods)
#     together in one class, and controls how they can be accessed from outside.

#     -   real-world analogy - think of an ATM machine:
#         - inside the ATM: Cash, card reader, computer system, cameras
#         - what you can access: keypad, screen, card slot, cash dispenser
#         - what you cannot access: internal cash sotrage, computer motherboard, security cameras
#     -   The ATM encapsulates all its internal components and only gives you safe ways to interact with it
# '''

# class NigerianBankAccount:
#     def __init__(self, owner, initial_balance=0):
#         self.owner = owner 
#         self._balance = initial_balance     # protected attribute
#         self.__pin = "1234"                 # private attribute
#         self._transaction_history = []      # protected attribute

#     # Public methods - anyone can use
#     def deposit(self, amount):
#         if amount > 0:
#             self._balance += amount 
#             self._transaction_history.append(f"Deposited N{amount:,}")
#             return f"N{amount:,} deposited successfully"
#         return "Invalid deposit amount"
    
#     def withdraw(self, amount, pin):
#         if self.__verify_pin(pin):
#             if amount <= self._balance:
#                 self._balance -= amount 
#                 self._transaction_history.append(f"Withdrew N{amount:,}")
#                 return f"N{amount:,} withdrawn successfully"
#             return "Insufficient funds"
#         return "Invalid PIN"
    
#     def check_balance(self, pin):
#         if self.__verify_pin(pin):      # uses private method
#             return f"Current balance: N{self._balance:,}"
#         return "Invalid PIN"
    
#     # Private method - only the class can use this
#     def __verify_pin(self, entered_pin):
#         return entered_pin == self.__pin 
    
#     # Protected method - subclasses can use this
#     def _get_transaction_history(self):
#         return self._transaction_history.copy()
    

# Using the encapsulated account
# ibrahim_account = NigerianBankAccount("Ibrahim Orekunrin", 50000)

# # These work - public interface
# print(ibrahim_account.deposit(10000))       # N10,000 deposited successfully
# print(ibrahim_account.withdraw(5000, "1234"))   #N5,000 withdrawn successfully
# print(ibrahim_account.check_balance("1234"))    # current balance: N55,000


# Try this out....
# But it won't work - private/protected data
# print(ibrahim_account.__pin)      # Error! cannot access private attribute
# ibrahim_account.__verify_pin("1234")      # Error! cannot access private method

# ''' Benefits of Encapsulation
#     -   Security: Sensitive data (like PIN) is protected
#     -   Organization: Related functions stay together
#     -   Control: You decide how data can be accessed
#     -   Maintenance: changes inside don't break outside code
# '''
# class Example:
#     def __init__(self):
#         self.public = "Anyone can access"       # Public
#         self._protected = "Subclasses can access"   # Protected (convention)
#         self.__private = "Only this class can access"   # Private (name mangling)


# ''' Abstraction
#     What is Abstraction?
#     Abstraction means hiding complex implementation details and showing
#     only the essential features. It's like using a remote control - you press 
#     buttons to change channels, but you don't need to know how to be a passenger

# '''
# from abc import ABC, abstractmethod 

# # Abstract base class - defines what a Nigerian Student should do
# class NigerianStudent(ABC):
#     def __init__(self, name, course, level):
#         self.name = name 
#         self.course = course 
#         self.level = level 
#         self.fees_paid = False 

#     # concrete method - all students can do this
#     def pay_school_fees(self, amount):
#         self.fees_paid = True 
#         return f"{self.name} paid N{amount:,} school fees"
    
#     # abstract method - each type of student implements differentely
#     @abstractmethod 
#     def study_method(self):
#         pass 

#     @abstractmethod 
#     def take_exam(self):
#         pass 

# # concrete classes - specific implementations
# class MedicalStudent(NigerianStudent):
#     def study_method(self):
#         return f"{self.name} studies anatomy books and practices on cadavers"
    
#     def take_exam(self):
#         return f"{self.name} takes practical exam in the anatomy lab"

# class EngineeringStudent(NigerianStudent):
#     def study_method(self):
#         return f"{self.name} solves mathematical problems and builds prototypes"
    
#     def take_exam(self):
#         return f"{self.name} takes exam with calculations and technical drawing"
    

# class ComputerScienceStudent(NigerianStudent):
#     def study_method(self):
#         return f"{self.name} codes programs and debugs software"
    
#     def take_exam(self):
#         return f"{self.name} takes practical programming exam on computer"
    
# # using abstraction
# students = [
#     MedicalStudent("Dr. Adeyinka Ogunsanya", "Medicine", 400),
#     EngineeringStudent("Dr. Ajala Gift", "Mechanical Engineering", 300),
#     ComputerScienceStudent("Fatima Hassan", "Computer Science", 200)
# ]

# # same interface, different implementations
# for student in students:
#     print(student.pay_school_fees(150000))      # same for all
#     print(student.study_method())               # different for each 
#     print(student.take_exam())                  # different for each
#     print("---")


# # Simple abstraction for phone interface
# class SimplePhone:
#     def __init__(self, brand):
#         self.brand = brand 
#         self._complex_internal_system = "Very complicated stuff"

#     # simple interface - user doesn't need to know internal complexity
#     def make_call(self, number):
#         self._establish_network_connection()
#         self._encode_voice_signal()
#         self._transmit_to_tower()
#         return f"Calling {number} from {self.brand} phone..."
    
#     def send_sms(self, message, number):
#         # self._connect_to_sms_center()
#         # self._format_message()
#         # self._send_through_network()
#         return f"SMS sent to {number}: '{message}'"
    
#     # complex internal methods - hidden from user
#     def _establish_network_connection(self):
#         # complex networking code here
#         pass 

#     def _encode_voice_signal(self):
#         # complex networking code here
#         pass 

#     def _transmit_to_tower(self):
#         # complex radio transmission here
#         pass 

# # user only needs to know the simple interface
# my_phone = SimplePhone("Tecno")
# print(my_phone.make_call("08012345678"))        # smiple to use
# print(my_phone.send_sms("How far na?\nHow u dey?", "08098765432"))      # don't need to know internals

# ''' Benefits of Abstraction
#     -   Simplicity: Complex systems become easy to use
#     -   Focus: users focus on what matters, not how it works
#     -   Flexibility: implementation can change without affecting users
#     -   Reusability: same interface works for different implementations

#     Inheritance - Building on What Already Exists
#     What is Inheritance?
#     Inheritance allows you to create new classes based on existing ones.
#     The new class (child) inherits attributes and methods from the parent
#     class, and can add it's own features or modify existing ones.
#     -   Real-World Analogy
#         - Think of a Nigerian family
#             - Parent(father): Adebayo Ogundimu - has surname, family traditions,
#             property
#             - Child 1 (Son): Kemi Ogundimu - inherits surname, traditions, gets
#             family property + adds his own career as doctor
#             - Child 2 (Daughter): Tunde Ogundimu - inherits surname, traditions,
#             gets family property + adds her own career as engineer
#     -   The children inherit from their father but also have their own unique characteristics
# '''

# # Parent class - Base Nigerian Person
# class NigerianPerson:
#     def __init__(self, first_name, last_name, state_of_origin):
#         self.first_name = first_name 
#         self.last_name = last_name 
#         self.state_of_origin = state_of_origin 
#         self.can_speak_english = True 

#     def introduce(self):
#         return f"My name is {self.first_name} {self.last_name} from {self.state_of_origin}"
    
#     def greet(self):
#         return "Good morning!"
    
#     def speak_local_language(self):
#         return "I speak my local language"
    
# # child class 1 - Nigerian Student inherits from Nigerian Person
# class NigerianStudent(NigerianPerson):
#     def __init__(self, first_name, last_name, state_of_origin, course, level):
#         # inherit parent's initialization
#         super().__init__(first_name, last_name, state_of_origin)
#         # add student-specifi attributes
#         self.course = course 
#         self.level = level 
#         self.cgpa = 0.0

#     # overried parent method with student-specific version
#     def introduce(self):
#         parent_intro = super().introduce()  # get parent's introduction
#         return f"{parent_intro}. I'm a {self.level} level {self.course} student"
    
#     # Add student-specific methods
#     def study(self):
#         return f"{self.first_name} is studying {self.course}"
    
#     def take_exam(self):
#         return f"{self.first_name} is writing {self.course} exam"
    
# # child class 2 - Nigerian worker inherits from NigerianPerson
# class NigerianWorker(NigerianPerson):
#     def __init__(self, first_name, last_name, state_of_origin, job_title, company):
#         super().__init__(first_name, last_name, state_of_origin)
#         self.job_title = job_title 
#         self.company = company 
#         self.salary = 0

#     def introduce(self):
#         parent_intro = super().introduce()
#         return f"{parent_intro}. I work as a {self.job_title} at {self.company}"
    
#     def work(self):
#         return f"{self.first_name} is working as a {self.job_title}"
    
#     def receive_salary(self, amount):
#         self.salary += amount 
#         return f"{self.first_name} received N{amount:,} salary"
    
# # child class 3 - Nigerian teacher (inherits from NigerianWorker)
# class NigerianTeacher(NigerianWorker):
#     def __init__(self, first_name, last_name, state_of_origin, subject, school):
#         # teacher is a type of worker
#         super().__init__(first_name, last_name, state_of_origin, "Teacher", school)
#         self.subject = subject 
#         self.students = []

#     def introduce(self):
#         return f"My name is {self.first_name} {self.last_name} from {self.state_of_origin}. I teach {self.subject} at {self.company}"
    
#     def teach(self):
#         return f"Teacher {self.first_name} is teaching {self.subject}"
    
#     def grade_students(self):
#         return f"Teacher {self.first_name} is grading {self.subject} assignments"
    

# # using inheritance
# # create different types of people
# student = NigerianStudent("Kemi", "Adebayo", "Lagos State", "Computer Science", 300)
# worker = NigerianWorker("Chinedu", "Okafor", "Anambra State", "Software Developer", "Sail Innovation Lab")
# teacher = NigerianTeacher("Chris", "Ekwugum", "Lagos State", "Data Science", "Sail Innovation Lab")

# # all inherit basic Nigerian person abilities
# print("===Basic Inherited Methods===")
# print(student.greet())          # good morning (inherited)
# print(worker.speak_local_language())    # i speak my local language (inherited)
# print(teacher.greet())          # good morning (inherited)

# print("\n=== Customized Introductions ===")
# print(student.introduce())      # customized for students
# print(worker.introduce())       # customized for workers
# print(teacher.introduce())      # customized for teachers

# print("\n===Specific Abilities===")
# print(student.study())          # only students can do this
# print(worker.work())            # only workers can do this
# print(teacher.teach())          # only teachers can do this


# ''' Inheritance Heirarchy Visualization
#     NigerianPerson (Parent)
#     ├── Attributes: first_name, last_name, state_of_origin
#     ├── Methods: introduce(), greet(), speak_local_language()
#     │
#     ├── NigerianStudent (Child)
#     │   ├── Inherits: All parent attributes and methods
#     │   ├── Adds: course, level, cgpa
#     │   └── Adds: study(), take_exam()
#     │
#     ├── NigerianWorker (Child)
#     │   ├── Inherits: All parent attributes and methods
#     │   ├── Adds: job_title, company, salary
#     │   ├── Adds: work(), receive_salary()
#     │   │
#     │   └── NigerianTeacher (Grandchild)
#     │       ├── Inherits: Everything from NigerianWorker + NigerianPerson
#     │       ├── Adds: subject, students
#     │       └── Adds: teach(), grade_students()
# '''

# # Types of Inheritance
# # 1. Single Inheritance - one parent
# class Parent:
#     pass 

# class Child(Parent):        # child inherits from Parent
#     pass 

# # 2. Multiple Inheritance - Multiple parents
# class Father:
#     def father_trait(self):
#         return "Strong"

# class Mother:
#     def mother_trait(self):
#         return "Caring"
    
# class Child (Father, Mother):    # inherits from both parents
#     pass 

# child = Child()
# print(child.father_trait())     # Strong
# print(child.mother_trait())     # Caring


''' Benefits of Inheritance
    -   Core Reuse: Don't write the same code multiple times
    -   Organization: Related classes are grouped logically
    -   Maintenance: Fix bugs in parent class, all children benefit
    -   Extensibility: easy to add new types without changing existing code
'''

# How All (Abstraction, Encapsulation, Inheritance) Work Together
# Nigerian School Management System

# Abstraction - Define what all school members should do
from abc import ABC, abstractmethod 

class SchoolMember(ABC):
    def __init__(self, name, id_number):
        self._name = name           # encapsulation - protected attribute
        self._id_number = id_number     # encapsulation - protected attribute
    
    @abstractmethod 
    def daily_activity(self):       # abstraction - must be implemented
        pass 

    def get_info(self):             # common method for all
        return f"Name: {self._name}, ID: {self._id_number}"
    
# Inheritance - student inherits from schoolmember
class Student(SchoolMember):
    def __init__(self, name, id_number, class_level):
        super().__init__(name, id_number)       # inheritance
        self.__grades = []          # encapsulation - private

    def daily_activity(self):       # abstraction - implementation
        return f"{self._name} attends classes and studies"

    def add_grade(self, subject, score):    # encapsulation - controlled access
        if 0 <= score <= 100:
            self.__grades.append({"subject": subject, "score": score})
            return f"Grade added: {subject} = {score}"
        return "Invalid grade"
    
    def get_average(self):
        if self.__grades:
            total = sum(grade["score"] for grade in self.__grades)
            return total / len(self.__grades)
        return 0
    
# Inheritance - Teacher inherits from SchoolMember
class Teacher(SchoolMember):
    def __init__(self, name, id_number, subject):
        super().__init__(name, id_number)
        self.__subject = subject            # encapsulation - private

    def daily_activity(self):               # abstraction - implementation
        return f"{self._name} teaches {self.__subject} and grades assignment"
    

# using all three principles together
student = Student("Adunni Olaleye", "STU001", "SS2")
teacher = Teacher("Mr. Emeka Nwosu", "TCH001", "Mathematis")


# Polymorphism - same method, different behavior
print(student.daily_activity())     # student-specific activity
print(teacher.daily_activity())     # teacher-specific activity

# Encapsulation - controlled access to data
print(student.add_grade("Mathematics", 85))     # grade added
print(student.add_grade("English", 78))         # grade added
print(f"Average: {student.get_average()}")      # average: 

# can't access private data directly
# print(student.__grades)     # this would cause an error