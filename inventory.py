import os
import time

inventory = []

try:
 f = open("inventory.txt", "r")
 inventory = eval(f.read())
 f.close()
except:
 pass

def addItem():
 time.sleep(1)
 os.system("clear")
 print("Inventory")
 print()
 item = input ("item to add > ").capitalize()
 inventory.append(item)
 print("added")

def viewItem():
 time.sleep(1)
 os.system("clear")
 print("Inventory")
 print()
 seen = [] #counting items
 for item in inventory:
  if item not in seen:
   print(f"{item}{inventory.count(item)}")
   seen.append(item)

time.sleep(2)
             
def removeItem():
 time.sleep(1)
 os.system("clear")
 print("Inventory")
 print()
 item = input ("item to remove > ").capitalize()
 if item in inventory:
  inventory.remove(item)
  print("removed")
 else:
  print("you dont have the item")

while True:
 time.sleep(1)
 os.system("clear")
 print("Inventory")
 print()
 menu = input("1: Add\n2: View\n3: Remove\n> ")
 if menu =="1":
  addItem()
 elif menu == "2":
  viewItem()
 else:
  removeItem()


 f = open("inventory.txt", "w")
 f.write(str(inventory))
 f.close()
