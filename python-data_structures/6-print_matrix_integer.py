#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for i in range(0, len(matrix)):
        for j in matrix[i]:
            print("{:d}".format(j), end="")
            if j is not matrix[i][-1]:
                print(" ", end="")
        print("")
