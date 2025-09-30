while True:
    print("Left or right?")
    direction = input("> ")
    if direction == "left":
        print("You have chosen bad")
        break
    elif direction == "right":
# start the loop again
        continue
    else:
        print("No direction, clever, You won")
#stop the program
        exit()
#in case of break the loop
print("Game Over")
    