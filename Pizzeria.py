import os, time

pizza = []

try:
 f = open("pizza.txt", "r")
 pizza = eval(f.read())
 f.close()

except:
    print("No previous pizza data found. Starting fresh.")

def viewPizza():
 h1 = "Topping"
 h2 = "Size"
 h3 = "Quantity"
 h4 = "Total Price"
 print(f"{h1:<15}{h2:<10}{h3:<10}{h4:<10}")
 for row in pizza:
    print(f"{row[0]:<15}{row[1]:<10}{row[2]:<10}{row[3]:<10}")
    time.sleep(5)
  
def addPizza():
 time.sleep(1)
 os.system("clear")
name = input("Enter topping name: ")
toppings = int(input("Enter topping price: "))
size = input("Enter topping size: ").lower()
while True:
  try:
    qty = int(input("Enter topping quantity: "))
    break
  except:
    print(ValueError)
    
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


while True:
   time.sleep(1)
   os.system("clear")
   print("Current Pizza Toppings:")
   menu = input("Enter a topping to add 1 (or '2' to see): ")
   if menu == "1":
    addPizza()
   else:
    viewPizza()
    f = open("pizza.txt", "w")
    f.write(str(pizza))
    f.close()


