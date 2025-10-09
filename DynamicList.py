myAgenda =[]

def printList():
  for item in myAgenda:
    print(item)

while True:
  menu = input("Add or remove?: ")
  if menu == "add":
    item = input("Item to add: ")
    myAgenda.append(item)
  elif menu == "remove":
    item = input("Item to remove: ")
    myAgenda.remove(item)
  printList()
