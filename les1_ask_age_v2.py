# !/usr/bin/env python3
import datetime
import dateutil.relativedelta
import sys

def quit(str):
    if str == "quit":
        sys.exit(0)

today = datetime.datetime.today()
name = input("What's your name? ")
quit(name)
MONTHS_31 = (1, 3, 5, 7, 8, 10, 12)
MONTHS_30 = (4, 6, 9, 11)

print(f"{name}, please enter a date by the requested order :")

while True:
    year = input("Please enter the year (YYYY): ")
    quit(year)
    if not year.isdigit() or len(year) != 4 or int(year) <= 1900:
        print(f"Wrong input {name}. Try again")
        continue

    month = input("Please enter the month (MM): ")
    quit(month)
    if not month.isdigit() or int(month) >= 13:
        print(f"Wrong month input {name}. Try again from start")
        continue

    day = input("Please enter the day (DD): ")
    quit(day)
    check = True
    if not day.isdigit():
        check = False
    if int(month) in MONTHS_31 and int(day) > 31 or \
            int(month) in MONTHS_30 and int(day) > 30 or \
            int(month) == 2 and int(day) > 28 and int(year)%4 != 0 or \
            int(month) == 2 and int(day) > 29 and int(year)%4 == 0:
        check = False

    if not check:
        print(f"Wrong input {name}. Try again ")
        continue

    break

birthday = datetime.datetime(int(year), int(month), int(day))
difference_in_years = dateutil.relativedelta.relativedelta(today, birthday).years

if difference_in_years >= 18:
    print(f"You are adult. Welcome {name}! ")
else:
    print(f"Sorry {name} you are underage ")