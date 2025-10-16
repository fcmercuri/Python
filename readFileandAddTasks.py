import os, time, random

def add():
    os.system("clear")
    idea = input("Enter your idea: ")
    f = open("ideas.txt", "a+") #a vs a+ (+) creates the file if it doesn't exist
    f.write(f"{idea}\n")
    f.close()
    time.sleep(1)
    os.system("clear")

def show():
    os.system("clear")
    f = open("ideas.txt", "r")
    ideas = f.read().split("\n")
    f.close()
    ideas.remove("")
    idea = random.choice(ideas)
    print(idea)
    time.sleep(2)
    os.system("clear")
    

while True:
    menu = input("1: Add idea\n2: Show a random idea\n>")
    if menu == "1":
        add()
    else:
        show()
