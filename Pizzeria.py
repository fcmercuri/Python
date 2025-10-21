import os
import time

pizza = []

try:
    with open("pizzas.txt", "r") as f:
        pizza = eval(f.read())
except (FileNotFoundError, SyntaxError):
    print("No previous pizza data found. Starting fresh.")

def viewPizza():
    os.system("cls" if os.name == "nt" else "clear")
    h1 = "Topping"
    h2 = "Size"
    h3 = "Quantity"
    h4 = "Total Price"
    print(f"{h1:<15}{h2:<10}{h3:<10}{h4:<10}")
    if not pizza:
        print("No pizzas in the order yet.")
    else:
        for row in pizza:
            print(f"{row[0]:<15}{row[1]:<10}{row[2]:<10}{row[3]:<10}")
    time.sleep(2)

def addPizza():
    os.system("cls" if os.name == "nt" else "clear")
    name = input("Enter topping name: ")
    # The 'toppings' variable seems to be unused, it has been commented out.
    # toppings = int(input("Enter topping price: "))
    
    size = ""
    while size not in ["small", "medium", "large"]:
        size = input("Enter topping size (small, medium, or large): ").lower()
    
    while True:
        try:
            qty = int(input("Enter topping quantity: "))
            if qty > 0:
                break
            else:
                print("Quantity must be a positive number.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")

    cost = 0
    if size == "small":
        cost = 5.99
    elif size == "medium":
        cost = 7.99
    else:
        cost = 9.99
    
    total = cost * qty
    total = round(total, 2)
    row = [name, size, qty, total]
    pizza.append(row)
    print(f"\nAdded {qty} {size} pizzas with {name} topping.")
    time.sleep(2)

while True:
    os.system("cls" if os.name == "nt" else "clear")
    print("Pizza Order Menu")
    print("----------------")
    menu = input("Enter '1' to add a pizza, '2' to view order, or '3' to exit: ")
    
    if menu == "1":
        addPizza()
    elif menu == "2":
        viewPizza()
    elif menu == "3":
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
        time.sleep(2)

# Save the data before exiting
try:
    with open("pizzas.txt", "w") as f:
        f.write(str(pizza))
    print("\nPizza order saved to pizzas.txt. Goodbye!")
except IOError:
    print("\nCould not save pizza data to file.")
