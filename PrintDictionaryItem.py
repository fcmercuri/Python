john = {"daysCompleted": 3, "daysRemaining": 3}
erica = {"daysCompleted": 4, "daysRemaining": 2}
courseProgress = {"Erica": erica, "john": john}

print(courseProgress["Erica"]["daysCompleted"])
