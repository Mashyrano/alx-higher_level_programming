#!/usr/bin/python3
def print_matrix_integer(matrix = [[]]):
    for i in matrix:
        for j in range(len(i)):
            if j < len(i) - 1:
                print(i[j], end=" ")
            else:
                print(i[j], end="")
        print("$")
