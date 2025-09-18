#ask user for input using a variable
username =  input("What's your name?: ")
password = input("What's your password?: ")

#if statement always double equal, elif, else
if username == "David":
    print("Welcome", username)
elif username == "Francesco" and password == "1234":
    print("You are in ",  username)
elif username == "Ari":
    print("Nooo ", username)
else:
    print("Out")

          
          
#nested alternative

#ask user for input using a variable with or
username =  input("What's your name?: ")

if username == "Peppa" or username == "peppa":
    print("Welcome", username)
    movie = input("Are you peppa pig?: ")
    if movie == "Yes":
        print("Me too")
    else:
        print("Sorry I am stupid")
elif username == "Francesco":
    print("You are in ",  username)
elif username == "Ari":
    print("Nooo ", username)
else:
    print("Out")