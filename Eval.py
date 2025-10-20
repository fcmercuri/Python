myEvents = []

f = open("events.txt", "r")
myEvents = eval(f.read()) #eval() converts string representation of list back to list
f.close()         

def prettyPrint():
    print()
    for row in myEvents:
        print(f"{row[0]:^15} {row[1]:^15}")
    print()

while True:
 menu = input("(1)Add event, (2)Remove event\n")
 if menu =="1":
    event = input("Enter event name: ").capitalize()
    date = input("Enter event date (DD/MM/YYYY): ")
    row = [event, date]
    myEvents.append(row)
    prettyPrint()
 else:
    criteria = input("Enter event name to remove: ").title()
    for row in myEvents:
        if criteria in row:
            myEvents.remove(row)
    prettyPrint()

 f = open("events.txt", "w")
 f.write(str(myEvents))
 f.close()         
         
    
