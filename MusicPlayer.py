import os, time

print("MyPOD Music Player")

def player():
    print("Press 1 to Play")
    print("Press 2 to Exit")
    print("Press other number to see the menu again")
    
    press = int(input("Choose an option: "))

    return press

while True:
    press = player()
    if press == 1:
        print("Playing Music 🎵")
        print()
        time.sleep(1)
        os.system("clear")
    elif press == 2:
        print("Exit")
        print()
        break
    else:
        os.system("clear")
        continue
