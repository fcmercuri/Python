import random
def health_hp():
  while True:
    firstroll = random.randint(1,6)*random.randint(1,6)
    secondroll = random.randint(1,8)*random.randint(1,6)
    health = firstroll*secondroll
    characters_name = input("characters name!\n>")
    print(characters_name,'have',health,"HP")
    wanna_go_again = input("wanna go again? n/y \n>")
    if wanna_go_again == "n":
      break
    else:
      continue
      return health

health_hp()
