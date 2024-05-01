#!/usr/bin/python3

print("01", end="")
for i in range(0, 10):
    for j in range(0, 10):
        j += i
        if ((i != j) and (j < 10) and not (i == 0 and j == 1)):
            print(", {}{}".format(i, j), end="")
print("")
