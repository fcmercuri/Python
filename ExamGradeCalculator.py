print("=== Exam Grade Calculator")
yourScore = int(input("What's your score? "))

if yourScore >= 90:
    print("Your grade is A+")
elif yourScore >= 80 and yourScore < 90:
    print("Your grade is A-")
elif yourScore >= 70 and yourScore < 80:
    print("Your grade is B")
else:
    print("Your grade is no pass")
