#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    real = 0
    for i in range(0, x):
        try:
            print("{}".format(my_list[i]), end="")
            real = real + 1
        except Exception:
            break
    print("")
    return real
