#!/usr/bin/env python3

fist_digit = int(input('your fist digit: '))
second_digit = int(input('your second digit: '))
operation = input('your operation ["+", "-", "*" or "/"]: ')

def arithmetic(fist_digit, second_digit, operation):
    if fist_digit == 0 and operation == "/":
        return 'UCD0'

    if operation == "/":
        return fist_digit / second_digit
    elif operation == "*":
        return fist_digit * second_digit
    elif operation == "-":
        return fist_digit - second_digit
    elif operation == "+":
        return fist_digit + second_digit
    else:
        return 'OU'

res = arithmetic(fist_digit, second_digit, operation)

if res == 'UCD0':
    print("You can't divide on zero")
elif res == 'OU':
    print('Operation underfined')
else:
    print(f"Your result is {res}")
