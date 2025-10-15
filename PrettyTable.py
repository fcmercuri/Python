list = []

def print_list():
    print()
    for row in list:
      for item in row:
        print(f"{item:^10}", end=" | ")
      print()
    print()

while True:
    name = input("Enter name: ")
    age = input("Enter age: ")
    job = input("Enter job: ")
    row = [name, age, job]
    list.append(row)
    exit = input("Do you want to exit? (y/n): ")
    if(exit.strip().lower()[0]=="y"):
        break

print_list()
