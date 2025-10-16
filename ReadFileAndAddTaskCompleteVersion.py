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
    menu = input("1: Add idea\n2: Show a random idea\n3: Print all ideas\n4: Exit\n>")
    if menu == "1":
        add()
    elif menu == "2":
        show()
    elif menu == "3":
        os.system("clear")
        try:
            with open("ideas.txt", "r") as f:
                all_ideas = f.read().split("\n")
                all_ideas = [idea for idea in all_ideas if idea]

            print("--- Your Saved Ideas ---")
            if not all_ideas:
                print("No ideas saved yet.")
            else:
                for idx, idea in enumerate(all_ideas, 1):
                    print(f"{idx}. {idea}")
            print("------------------------")
            time.sleep(3)
            os.system("clear")
        except FileNotFoundError:
            print("No ideas.txt file found.")
            time.sleep(2)
            os.system("clear")
    elif menu == "4":
        print("Exiting program.")
        break
    else:
        print("Invalid option. Please try again.")
        time.sleep(1)
        os.system("clear")

