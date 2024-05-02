#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

    def add(a, b):
        return a + b

    r = 0

    if len(argv) == 1:
        print("0")
    else:
        for i in range(1, len(argv)):
            r = add(r, int(argv[i]))
        print(f"{r}")
