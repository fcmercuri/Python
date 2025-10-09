list = ["Math", "Science", "History", "Art"]
print(list[0]) # Output: Math

list[3] = "Physical Education"
print(list) # Output: ['Math', 'Science', 'History', 'Physical Education']

for lesson in list:
    print(lesson) # Output: Math Science History Physical Education (each on a new line)

print(f"The first subject is {list[0]}") # Output: The first subject is Math

import random
greetings = ["Hello", "Hi", "Hey", "Greetings", "Salutations"]
index = random.randint(0, len(greetings) - 1)
print(greetings[index]) # Output: Random greeting from the list
