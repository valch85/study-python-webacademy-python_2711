#!/usr/bin/env python3

def is_prime(digit):
    digit = int(digit)
    if digit == 0 or digit == 1:
        return False

    if digit == 2:
        return True

    i = 2
    while i < digit:
        if digit%i == 0:
            return False
        else:
            i += 1
    return True

digit = input('Please enter a number:')

if is_prime(digit) == True:
    print('didgit is prime number')
else:
    print('didgit is composite number')


