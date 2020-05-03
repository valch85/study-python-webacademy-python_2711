#!/usr/bin/env python3

def check_seasons(month):
    seasons = {
        'winter': (12, 1, 2),
        'summer': (6, 7, 8),
        'fall': (9, 10, 11),
        'spring': (3, 4, 5)
    }


    for season_name, month_digit in seasons.items():
        if month in month_digit:
            return season_name

    return 'error'

def exit(month):
    if month == 'quit' or month == 'exit':
        return False

while True:
    month = (input('enter month MM: '))

    if exit(month) == False:
        break

    res = check_seasons(int(month))
    print(res)
    break
