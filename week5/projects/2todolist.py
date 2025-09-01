from pathlib import Path
# 2, 13, 17
"""
A to-do list application is a practical project that
 helps users manage tasks efficiently. This application allows
 users to add, remove, and view tasks while keeping track of
 completed and pending activities. Learning to build a to-do
 list enhances understanding of data structures, file
 handling, and basic user interaction in Python.
 This project will cover step-by-step implementation of a to
do list application, user input handling, list operations, and
 file handling for persistent storage.

 Key Concepts of To-Do List in Python
 Basic List Operations:
 -Adding tasks
 -Removing tasks
 -Marking tasks as complete
 -Displaying tasks
 -User Input Handling:
 -Using input() function
 -Handling invalid inputs
 File Handling:
 -Storing tasks in a text file
 -Retrieving saved tasks on program
 restart
 Functions in Python:
 -Defining functions for task management
 -Calling functions with user inputs
"""


new = Path("workspace")
new.mkdir(exist_ok=True)
file_path = new / "to_do_list.txt"
file_path.touch()

tasks = []



def add_task(task):
    tasks.append(task)
    return f"Task {task} added"
    

def rm_task(task):
    if task in tasks:
        tasks.remove(task)
        return f"Task {task} removed"
    return f"task not found"

def dis_task(task):
    for task in tasks:
        print(task)



while True:
    print("""1. Add Task
    2. Remove Task
    3. View Tasks
    4. Close""")

    try:
        choice = int(input("input option: "))
        if choice == 1:
            to_add = input("Enter task to add: ")
            print(add_task(to_add))
        elif choice == 2:
            to_rm = input("Enter task to remove: ")
            print(rm_task(to_rm))
        elif choice == 3:
            print(f"Tasks are: {dis_task}")
        elif choice == 4:
            print("Exiting... Thank you")
            break 
        else:
            print("Invalid input")
            
        with open(file_path, "r", newline="", encoding="utf-8") as f:
            f.write(tasks)

    except ValueError as ve:
        print ("Error! Input the correct option", ve)

