print("welcome to number guessing game")

mynum = 456
counter = 0

while True:
  num = int(input("guess a num between 1 to 1000: "))
  if num > 456:
    print("num is too high. try again")
    counter += 1
    continue
  elif num < 456 and num > 0:
    print("num is too low. try again")
    counter += 1
    continue
  elif num < 0:
    print("num is negative")
    exit()
  else:
    print("you guessed right.")
    print("you had", counter, "chances")
    break
print("Game over")
