import random, time
def rollDice (sides):
    result=random.randint(1,sides)
    return result
    
def health():
    health_score = (rollDice(6)*rollDice(12)/2)+10
    return health_score

def strength():
    strength_score = (rollDice(6)*rollDice(8)/2) +12
    return strength_score
    
print("Mortal Combat")
time.sleep(1)
name1 = input ("Name your legend \n")
type1 = input ("Character type (Human, Elf, Wizard, Orc): \n")
health1 = health()
strength1 = strength()
print (name1)
print ("Health:", health1)
print ("strength:", strength1)
print()
time.sleep(1)
print ("His opponent")
time.sleep(1)
print()
name2 = input ("Name your legend \n")
type2 = input ("Character type (Human, Elf, Wizard, Orc): \n")
health2 = health()
strength2 = strength()
print (name2)
print ("Health:", health2)
print ("strength:", strength2)
print()
time.sleep(1)
round = 0
while health1 > 0 and health2 > 0:
    round = round + 1
    print("Round", round)
    print ("The battle begins!!")
    name1rd = rollDice(6)
    #print (name1, "rolled", name1rd)
    name2rd = rollDice(6)
   #print (name2, "rolled", name2rd)
    if name1rd > name2rd:
        health2 = health2 - name1rd
        print (name1, "Won round", round)
        print (name2, "'s health remaining", health2)
    elif name1rd < name2rd:
        health1 = health1 - name2rd
        print (name2, "Won round", round)
        print (name1, "'s health remaining", health1)
    else:
        print("It is a draw")
    time.sleep(1)
    print()
    if health1 <= 0:
        print (name2, "is the winner")
        print ("After", round, "rounds", name2, "beats", name1)
        break
    elif health2 <= 0:
        print (name1, "is the winner")
        print ("After", round, "rounds", name1, "beats", name2)
        break
exit()
