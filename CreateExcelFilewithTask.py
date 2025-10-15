import os
import time
import pandas as pd

toDo = []
EXCEL_FILE = "todo.xlsx"

def clear_screen():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def load_from_excel():
    """Loads tasks from an Excel file if it exists."""
    global toDo
    if os.path.exists(EXCEL_FILE):
        try:
            df = pd.read_excel(EXCEL_FILE)
            toDo = df.values.tolist()
            print("To-do list loaded from Excel.")
        except Exception as e:
            print(f"Error loading file: {e}")
            toDo = [] # Reset list if there's an error
    else:
        print("No existing Excel file found. Starting with an empty list.")
    time.sleep(1)

def save_to_excel():
    """Saves the current to-do list to an Excel file."""
    if not toDo:
        print("No tasks to save.")
        time.sleep(1)
        return
    
    df = pd.DataFrame(toDo, columns=["Task", "Due Date", "Priority"])
    df.to_excel(EXCEL_FILE, index=False)
    print("To-do list saved to Excel.")
    time.sleep(1)

def add():
    """Adds a new task to the list."""
    clear_screen()
    name = input("Enter task name: ")
    date = input("Enter due date: ")
    
    while True:
        priority = input("Enter priority (1-5): ")
        if priority.isdigit() and 1 <= int(priority) <= 5:
            break
        print("Invalid priority. Please enter a number between 1 and 5.")
        
    row = [name, date, priority]
    toDo.append(row)
    print("Task added!")
    time.sleep(1)

def view():
    """Displays tasks, either all or filtered by priority."""
    clear_screen()
    option = input("1: View all\n2: View by priority\n")
    print("-" * 30)
    print("Task | Due Date | Priority")
    print("-" * 30)
    
    if option == "1":
        if not toDo:
            print("No tasks in list.")
        for row in toDo:
            print(" | ".join(row))
    elif option == "2":
        priority = input("Enter priority (1-5): ")
        found = False
        for row in toDo:
            if priority in row:
                print(" | ".join(row))
                found = True
        if not found:
            print(f"No tasks found with priority '{priority}'.")
    else:
        print("Invalid option.")
    
    print("-" * 30)
    time.sleep(3)

def edit():
    """Edits an existing task."""
    clear_screen()
    find = input("Enter task name to edit: ").lower()
    
    # Find all matching tasks and present them
    found_tasks = [row for row in toDo if find in row[0].lower()]
    if not found_tasks:
        print("Could not find task.")
        time.sleep(1)
        return

    print("Found matching tasks:")
    for i, task in enumerate(found_tasks):
        print(f"{i+1}: {task[0]} | Due: {task[1]} | Priority: {task[2]}")
    
    try:
        task_index_to_edit = int(input("Enter the number of the task to edit: ")) - 1
        if 0 <= task_index_to_edit < len(found_tasks):
            original_task = found_tasks[task_index_to_edit]
            print(f"Editing: {original_task[0]}")
            
            new_name = input(f"Enter new task name (or leave blank to keep '{original_task[0]}'): ") or original_task[0]
            new_date = input(f"Enter new due date (or leave blank to keep '{original_task[1]}'): ") or original_task[1]
            
            while True:
                new_priority = input(f"Enter new priority (1-5) (or leave blank to keep '{original_task[2]}'): ")
                if not new_priority:
                    new_priority = original_task[2]
                    break
                if new_priority.isdigit() and 1 <= int(new_priority) <= 5:
                    break
                print("Invalid priority. Please enter a number between 1 and 5.")

            # Find the original task's position in the main list and update it
            for i, row in enumerate(toDo):
                if row == original_task:
                    toDo[i] = [new_name, new_date, new_priority]
                    break
            print("Task updated!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")
    time.sleep(2)

def remove():
    """Removes a task from the list."""
    clear_screen()
    find = input("Enter task name to remove: ").lower()
    
    found_tasks = [row for row in toDo if find in row[0].lower()]
    if not found_tasks:
        print("Could not find task.")
        time.sleep(1)
        return

    print("Found matching tasks:")
    for i, task in enumerate(found_tasks):
        print(f"{i+1}: {task[0]} | Due: {task[1]} | Priority: {task[2]}")
    
    try:
        task_index_to_remove = int(input("Enter the number of the task to remove: ")) - 1
        if 0 <= task_index_to_remove < len(found_tasks):
            original_task = found_tasks[task_index_to_remove]
            toDo.remove(original_task)
            print("Task removed!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")
    time.sleep(2)

# Load data when the script starts
load_from_excel()

while True:
    clear_screen()
    menu = input("1: Add\n2: View\n3: Edit\n4: Remove\n5: Save\n6: Exit\n")
    if menu == "1":
        add()
    elif menu == "2":
        view()
    elif menu == "3":
        edit()
    elif menu == "4":
        remove()
    elif menu == "5":
        save_to_excel()
    elif menu == "6":
        save_to_excel() # Optional: save before exiting
        print("Exiting program.")
        break
    else:
        print("Invalid option. Please try again.")
        time.sleep(1)
