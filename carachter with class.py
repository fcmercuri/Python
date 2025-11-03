class character:
    name = None
    health = 100
    mp = 100

    def __init__(self, name):
        self.name = name

    def print(self):
        print(f"{self.name}\tHP: {self.health}\tMP:{self.mp}")

    def setStats(self, health, mp):
        self.health = health
        self.mp = mp

class player(character):
    nickname = None
    lives = 3

    def __init__(self, nickname, lives):
        # Explicitly call the parent class's __init__ method using super()
        super().__init__('Player') # Pass a default name to the character constructor
        self.nickname = nickname
        self.lives = lives

    def print(self):
        print(f"{self.name}\tHP: {self.health}\t MP:{self.mp}\tNickname: {self.nickname}\tLives: {self.lives}")

    def isAlive(self):
        if self.lives > 0:
            print(f"{self.nickname} is alive")
            return True
        else:
            print(f"{self.nickname} is dead")
            return False

# Create an instance of the 'player' class
# The string argument was missing quotes, and a second argument was needed for 'lives'
ian = player('Ian the great', 3) 
ian.print()
print(ian.isAlive())

class enemy(character):
    type = None
    strength = None

    def __init__(self, name, type, strength):
        # Call the parent class's __init__ method
        super().__init__(name) 
        self.type = type
        self.strength = strength

    def print(self):
        print(f"{self.name}\tHP: {self.health}\t MP:{self.mp}\tType: {self.type}\tStrength: {self.strength}")

class orc(enemy):
    speed = None

    def __init__(self, speed):
        self.name = "Orc"
        self.type = "Orc"
        self.strength = 200
        self.speed = speed

    def print(self):
        print(f"{self.name}\tHP: {self.health}\t MP:{self.mp}\tType: {self.type}\tStrength: {self.strength}\tSpeed: {self.speed}")
    
sharron = orc(250)
gary = orc(205)

sharron.print()
gary.print()

class vampire(enemy):
    day = True

    def __init__(self, day):
     self.name = "Vampire"
     self.type = "Vampire"
     self.strength = 150
     self.day = day
    
    def print(self):
        print(f"{self.name}\tHP: {self.health}\t MP:{self.mp}\tType: {self.type}\tStrength: {self.strength}\tDay: {self.day}")
    

eric=vampire(False)
eric.print()

