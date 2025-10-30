import datetime

today = datetime.date.today()

print("Event Contdown")
day = int(input("Enter the day of the event (1-31): "))
month = int(input("Enter the month of the event (1-12): ")) 
year = int(input("Enter the year of the event (e.g., 2024): "))
event = datetime.date(year, month, day)

difference = event - today
difference = difference.days

if difference > 0:
    print(difference, "days until the event.")
elif difference < 0:
    print("The event has already passed.")    
else:
    print("The event is today!")
