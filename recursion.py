def reverse(value):
  if value <= 0:
    print("Done")
    return
  else:
    for i in range(value):
      print("🌹", end="")
    print()
    reverse(value-2)
reverse(5)
