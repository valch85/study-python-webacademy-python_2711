#!/usr/bin/env python3
import datetime
import dateutil.relativedelta

today = datetime.datetime.today()
print(today)
name = input("What's your name? ")

print (f"{name}, please enter a date by the requested order :")

while True:
    year = input("Please enter the year: ")
    if year.isdigit():
        break
    else:
        print(f"Wrong input {name}. Try again ")
        continue

while True:
    month = input("Please enter the month: ")
    if month.isdigit() and int(month) < 13:
        break
    else:
        print(f"Wrong input {name}. Try again ")
        continue

while True:
    day = input("Please enter the day: ")
    if day.isdigit() and int(day) < 31:
        break
    else:
        print(f"Wrong input {name}. Try again ")
        continue

birthday = datetime.datetime(int(year),int(month),int(day))
difference_in_years = dateutil.relativedelta.relativedelta(today, birthday).years

if difference_in_years >= 18:
    print(f"You are adult. Welcome {name}! ")
else:
    print(f"Sorry {name} you are underage ")
