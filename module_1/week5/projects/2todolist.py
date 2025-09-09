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

def work_path():
    folder_path = Path("workspace")
    folder_path.mkdir(exist_ok=True)
    file_path = folder_path / "to_do_list.txt"
    return file_path

tasks = []



def add_task(task):
    tasks.append(task)
    return f"Task '{task}' added"
    

def rm_task(task):
    if task in tasks:
        tasks.remove(task)
        return f"Task '{task}' removed"
    return f"task not found"



def save_task(path):
        with open(path, "w", newline="", encoding="utf-8") as f:
            f.write("To-do List\n")
            for task in tasks:
                f.write(f"{task}\n")

def view_task(path):
    if path.exists():
        with open(path, "r", newline="", encoding="utf-8") as f:
            return f.read()
    return "No tasks yet"

def load_task(path):
    if path.exists():
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                tasks.append(line.strip())


file_path = work_path()
while True:
    print("""
1. Add Task
2. Remove Task
3. View Tasks
4. Close""")

    try:
        choice = int(input("input option: "))
        if choice == 1:
            to_add = input("Enter task to add: ")
            print(add_task(to_add))
            save_task(file_path)

        elif choice == 2:
            to_rm = input("Enter task to remove: ")
            print(rm_task(to_rm))
            save_task(file_path)

        elif choice == 3:
            print(f"Tasks are {view_task(file_path)}")

        elif choice == 4:
            print("Exiting... Thank you")
            break 
        else:
            print("Invalid input")
            
        
           

    except ValueError as ve:
        print ("Error! Input the correct option", ve)

