f = open("tasks.list", "w") #write mode
what = input("What do you want to write in the file? ") 
f.write(what)
f.close()


f = open("todo.txt", "r") #read mode
while True:
  contents = f.readline() #read one line
  if contents == "": #without this line, it will be an infinite loop and will print blank lines
   break
  print(contents)

f.close()
