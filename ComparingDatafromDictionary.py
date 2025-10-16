import os, time, random

keyword = {}

keyword["insurance"] = {"Volume": 100, "Difficulty": 200, "Ranking": 5, "Conversion": 50}
keyword["home"] = {"Volume": 200, "Difficulty": 100, "Ranking": 7, "Conversion": 40}
keyword["card"] = {"Volume": 100, "Difficulty": 200, "Ranking": 1, "Conversion": 35}
keyword["home"] = {"Volume": 600, "Difficulty": 500, "Ranking": 10, "Conversion": 45}

while True:
  print("===TOP KEYWORD===")
  print()
  print("List")
  print()
  for key in keyword:
    print(key)
  user = input("Enter a keyword to see details\n> ")
  comp = random.choice(list(keyword.keys()))
  print("Comparing with", comp)

  print("Details for Volume, Difficulty, Ranking, Conversion")

  answer = input("> ")

  print(f"{user}: {keyword[user][answer]}")
  print(f"{comp}: {keyword[comp][answer]}")

  if keyword[user][answer] > keyword[comp][answer]:
    print(user, "better")
  elif keyword[user][answer] < keyword[comp][answer]:
    print(comp, "better")
  else:
    print("Similar")

  time.sleep(5)
  os.system("clear")
