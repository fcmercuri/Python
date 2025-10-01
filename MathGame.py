print("=== Math Game ===")

multiple = int(input("Name your multiple "))

score = 0

for i in range(1, 4):
    answer = int(input(f"What is {i} x {multiple}? "))
    if answer == i * multiple:
     print("Correct!")
     score += 1
    else:
     print("Wrong!")
     print(f"The correct answer is {i * multiple}")
print("Your final score is", score)
