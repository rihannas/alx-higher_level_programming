#!/usr/bin/python3

def print_last_digit(number):

    if number > 0:
        last = number % 10
    else:
        number = number * (-1)
        last = number % 10

    print(last, end="")
    return last

# getting the last digit could be done by diving the number by 10 and checking the reminder
