#!/usr/bin/python3

def print_last_digit(number):
    if type(number) is int:
        print("{}".format(abs(number) % 10), end="")
        return (abs(number) % 10)
