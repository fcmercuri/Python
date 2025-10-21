import traceback

debugMode = True
myStuff = []

try:
   f = open("event.me", "r")
   myStuff = eval(f.read())
   f.close() 

#if the code in try block fails, the except block will run and capture the error
except:
    print("No previous event file found.")
    if debugMode:
        print(traceback)

for row in myStuff:
        print(row)
