class animal:
    # The __init__ method is a constructor that initializes a new object
    def __init__(self, species, name, sound):
        # 'self' refers to the specific object instance being created
        self.species = species
        self.name = name
        self.sound = sound

# Create an object (instance) of the animal class
dog = animal("Canine", "Rex", "Woof")

# Print the attribute of the object
print(dog.species)
