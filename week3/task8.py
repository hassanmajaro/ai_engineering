''' Task 1
        Explain each outpuut of the program below
        Give 3 use cases or scenarios where you can apply the program below
        Write the code for 1 of the 3 use cases.
'''
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print(f"{num1} == {num2} : {num1 == num2}")
# This says num1 is equal to num2; then return true if it is and false if it's not
print(f"{num1} != {num2} : {num1 != num2}")
# This says num1 is not equal to num2; then return true if it is and false if it's not
print(f"{num1} > {num2} : {num1 > num2}")
# This says num1 is greater than num2; then return true if it is and false if it's not
print(f"{num1} < {num2} : {num1 < num2}")
# This says num1 is less than num2; then return true if it is and false if it's not
''' Use cases: 
    This program can be used the following cases:
    1.  It can be used for profit or loss
    2.  It can be used for age range classification
    3.  It can be used for eligibility check
'''
age = int(input("Input age: "))

infant = age < 1
toddlers = age >= 1 and age <= 3
child = age >= 4 and age <= 12
teenager = (age >= 13) and (age <= 19)
adult = age >= 20
print("Age classification")
print(f"Age: {age}\nInfant: {infant}\nToddlers: {toddlers}\nChild: {child}\nTeenager: {teenager}\nAdult: {adult}")

''' Task 2
    Comment the code below approximately, and using docstring, explain what the code is doing.
    Adapt the code to the case below
    Federal Government Scholarship Key Eligibility Requirements:
        Citizenship:
            Applicant must be a citizen of Nigeria
        Enrollment:
            Must be a registered, full-time undergraduate student in a recognized Nigerian university
        Other Scholarships:
            Applicants cannot be currently receiving any other scholarship from an entity in the Oil and Gas industrym whether national or international
        Academic Qualification:
            For undergraduate courses, applicants usually need five distinctions (As and Bs) in relevant subjects in their WAEC/WASSCE (May/June) exams, including English and Mathematics.
'''
name = input("Enter your name: ")       # This prompts the user to input their name
age = int(input("Enter your age: "))    # This prompts the user for their age
score = int(input("Enter your test score: "))   # This prompts the user to input their test score

eligibility = (age < 18) and (score > 70)   # This checks that if the User is less than 18 and score is greater than 70; it will be true if both condition is met, if not false
print(f"Candidate: {name}\nAge: {age}\nScore: {score}\nEligible: {eligibility}")

name = input("Enter your name: ")
citizenship = input("Are you a Nigerian citizen? (Yes/No): ").lower()
enrollment = input("Are you a full-time undergraduate in a Nigerian University? (Yes/No): ")
scholarship = input("Are you currently on any Oil and Gas Scholarship? (Yes/No): ")
waec_result = int(input("Enter the number of WAEC distinctions you have (including English & Maths) i.e A/B grades: "))

requirements = [
    (citizenship == "yes"),
    (enrollment == "yes"),
    (scholarship == "no"),
    (waec_result >= 5)
]

eligibility = True
for rule in requirements:
    eligibility = eligibility and rule

print("Scholarship Application Result")
print(f"Candidate name: {name}")
print(f"Nigeria? ")
print(f"FT Undergraduate? {enrollment}")
print(f"Been on Oil & Gas Scholarship: {scholarship}")
print(f"Number of distinctions: {waec_result}")
print(f"Eligible: {eligibility}")


''' Task 3: Online Store Cart Calculation
    Create a list of items (e.g., "Book", "Pen", "Bag") and another list of prices (e.g., 500, 100, 2000).
    Start with an empty cart total (cart_total = 0)
    use assignment operators (+=) to add the price of some items into cart_total
    Print the list of items and the total price using an f-string like this:
        Items: ['Book', 'Pen', 'Bag']
        Total Price: N600
'''
items = ["Book", "Pen", "Bag"]
prices = [500, 100, 2000]
cart_total = 0
cart_total += prices[0]
cart_total += prices[1]
print(f"Items: {items}")
print(f"Total Price: N{cart_total}")

''' Task 4: Student Record
    Create an empty dictionary called student
    Ask the user to input their name and age, then store them in the dictionary
    Add a list of scores (e.g., [70, 85, 90]) to the dictionary.
    Use a comparison operator to check if the student has passed (average score >= 50). Save the result (True/False) in the dictionary under the key "passed".
    Use a logical operator to check if the student is a teenager (age between 13 and 19). Save the result as "teenager".
    Print out the complete record in this format:
        Student Record:
            Name: John
            Age: 16
            Scores: [70, 85, 90]
            Passed: True
            Teenager: True
'''
student = {}
name = input("Enter your name: ")
age = int(input("Enter your age: "))
scores = [70, 85, 90]
average_score = (scores[0] + scores[1] + scores[2]) / 3
student = {
    "name" : name,
    "age" : age,
    "scores" : [70, 85, 90],
    "passed" : average_score >= 50,
}
teenager = age > 13 and age < 19

print(f"Student Record:\nName: {student['name']}\nAge: {student['age']}\nScores: {student['scores']}\nPassed: {student['passed']}\nTeenager: {teenager}")


''' Task 5: Store Inventory Update
    Create a dictionary called store with items and their available quantities
        store = {"Book": 10, "Pen": 20, "Bag": 5}
    Ask the user to input the item they want to buy (e.g., "Pen")
    Ask the user to input the quantity they want to purchase
    Use the assignment operator -= to update (reduce) the item quantity in the dictionary.
    Print the updated dictionary in this format:
        Before purchase: {'Book': 10, 'Pen': 20, 'Bag': 5}
        After purchase: {'Book': 10, 'Pen': 18, 'Bag': 5}
'''
store = {
    "Book" : 10,
    "Pen" : 20,
    "Bag" : 5
}

print(f"Before purchase: {store}")
buy = input("Input the item you want to buy (Book/Pen/Bag): ").capitalize()
quantity = int(input("How many? "))

store[buy] -= quantity
print(f"After purchase: {store}")