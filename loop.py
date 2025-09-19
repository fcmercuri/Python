#while loop with condition
exit = " "
while exit != "yes":
    print("Hello World")
    exit = input("Do you want to exit? (yes/no): ")

#while loop with counter
counter = 0
while counter < 5:
    print(counter)
    counter += 1


#while loop with break

while True:
    print("Program is running")
    goAgain = input("Do you want to continue? (yes/no): ")
    if goAgain == "no":
#exit the loop
        break
#and print
print("Program has ended")

#while loop with accumulation  
counter = 0
while True:
    answer = int(input("Enter a number: "))
    print("Adding up...")
    counter += answer
    print("Current total:", counter)
    addAnother = input("Do you want to add another number? (yes/no): ")
    if addAnother == "no":
        break
print("Final total:", counter)