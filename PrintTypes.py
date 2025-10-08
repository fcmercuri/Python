for i in range (0, 100):
    # Print numbers from 0 to 99 and print a space after each number
    print(i, end=' ')

# Print with format method 1
name = "francesco"
surname = "giuseppe"
age = "29"

print("My name is {} and surname is {} and I'm {} years old".format(name, surname, age))

# Print with format method 2
response = "My name is {name} and surname is {surname} and I'm {age} years old".format(name = name, surname = surname, age = age)
print(response)

# Print with format method 3
response = f"My name is {name} and surname is {surname} and I'm {age} years old"
print(response)


# Print with loop
for i in range(0, 10):
    print(f"Number {i: <3} of 10")  # Left aligned within 3 spaces


# Print with loop n2
for i in range(0, 10):
    print("Number {count} of 10".format(count = i))  # Using format method
