import os
import time

toDo = []

def clear_screen():
    # Clears the terminal screen
    os.system('cls' if os.name == 'nt' else 'clear')

def add():
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
    clear_screen()
    option = input("1: View all\n2: View by priority\n")
    print("-" * 30)
    print("Task | Due Date | Priority")
    print("-" * 30)

    if option == "1":
        for row in toDo:
            print(" | ".join(row))
    elif option == "2":
        priority = input("Enter priority (1-5): ")
        for row in toDo:
            if priority == row[2]:
                print(" | ".join(row))
    else:
        print("Invalid option.")

    print("-" * 30)
    time.sleep(3)

def edit():
    clear_screen()
    find = input("Enter task name to edit: ").lower()
    found_tasks = [row for row in toDo if find in row[0].lower()]

    if not found_tasks:
        print("Could not find task.")
        time.sleep(1)
        return

    print("Found tasks:")
    for i, task in enumerate(found_tasks):
        print(f"{i+1}: {task[0]} | {task[1]} | {task[2]}")

    try:
        task_index = int(input("Enter the number of the task to edit: ")) - 1
        if 0 <= task_index < len(found_tasks):
            task_to_edit = found_tasks[task_index]
            print(f"Editing: {task_to_edit[0]}")
            
            new_name = input(f"Enter new task name (or leave blank to keep '{task_to_edit[0]}'): ") or task_to_edit[0]
            new_date = input(f"Enter new due date (or leave blank to keep '{task_to_edit[1]}'): ") or task_to_edit[1]
            
            while True:
                new_priority = input(f"Enter new priority (1-5) (or leave blank to keep '{task_to_edit[2]}'): ")
                if not new_priority or (new_priority.isdigit() and 1 <= int(new_priority) <= 5):
                    new_priority = new_priority or task_to_edit[2]
                    break
                print("Invalid priority. Please enter a number between 1 and 5.")

            # Find the original task and update it
            for i, row in enumerate(toDo):
                if row == task_to_edit:
                    toDo[i] = [new_name, new_date, new_priority]
                    break
            print("Task updated!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")
    time.sleep(2)

def remove():
    clear_screen()
    find = input("Enter task name to remove: ").lower()
    found_tasks = [row for row in toDo if find in row[0].lower()]
    
    if not found_tasks:
        print("Could not find task.")
        time.sleep(1)
        return

    print("Found tasks:")
    for i, task in enumerate(found_tasks):
        print(f"{i+1}: {task[0]} | {task[1]} | {task[2]}")

    try:
        task_index = int(input("Enter the number of the task to remove: ")) - 1
        if 0 <= task_index < len(found_tasks):
            original_task = found_tasks[task_index]
            toDo.remove(original_task)
            print("Task removed!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")
    time.sleep(2)

while True:
    clear_screen()
    menu = input("1: Add\n2: View\n3: Edit\n4: Remove\n5: Exit\n")
    if menu == "1":
        add()
    elif menu == "2":
        view()
    elif menu == "3":
        edit()
    elif menu == "4":
        remove()
    elif menu == "5":
        print("Exiting program.")
        break
    else:
        print("Invalid option. Please try again.")
        time.sleep(1)
