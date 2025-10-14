myDictionary = { "brand": "Ford", "model": "Mustang", "year": 2004 }

for name, metric in myDictionary.items():
  print(name, metric)
  if(name == "year"):
    if(metric>2000):
      print("This is a new car")
    else:
      print("This is an old car")


car = { "brand": None, "model": None, "year": None }

for name, value in car.items():
  car[name] = input(f"Enter car {name}: ")

  print()
  for name, value in car.items():
    print(f"Car {name} is {value}")
