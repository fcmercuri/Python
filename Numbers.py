#define int number
myScore = int(input("What's your score?: "))
if myScore > 90:
    print("Great")
else:
    print("Try Again")

#define float (decimals) number
myScore = float(input("What's your score?: "))
if myScore > 90.54:
    print("Great")
else:
    print("Try Again")


#round number   
bill= float(input("Total bill amount?: "))
answer = bill / 3
print(round(answer, 3))
