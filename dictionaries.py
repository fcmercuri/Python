clue = {}

def PrettyPrint():
  print()
  for key, value in clue.items():
   print(key, value)

while True:
  name = input("Enter your true name: ")
  location = input("Enter your current location: ")
  weapon = input("Enter your weapon of choice: ")
  clue[name] = {"location": location, "weapon": weapon}
  print(clue)
    
  PrettyPrint()
