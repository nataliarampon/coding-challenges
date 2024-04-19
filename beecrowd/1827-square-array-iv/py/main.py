# -*- coding: utf-8 -*-

def print_matrix(size, matrix):
    for i in range(size):
        for j in range(size):
            print(matrix[i][j], end='')
        print('\n', end='')
    print('\n', end='')

def fill_middle(matrix, low_limit_center, high_limit_center):
    for i in range(low_limit_center, high_limit_center):
        for j in range(low_limit_center, high_limit_center):
            matrix[i][j] = 1

def fill_diagonals(size, matrix, low_limit_center):
    for i in range(low_limit_center):
        matrix[i][i] = 2
        matrix[i][size-i-1] = 3
    
    for i in range(high_limit_center, size):
        matrix[i][i] = 2
        matrix[i][size-i-1] = 3;

def fill_center(size, matrix):
    matrix[size//2][size//2] = 4

while True:
    try:
        size = int(input())
        matrix = [[0 for _ in range(size)] for _ in range(size)]

        low_limit_center = size//3
        high_limit_center = 2*size//3 + (1 if size%3 else 0)

        fill_middle(matrix, low_limit_center, high_limit_center)

        fill_diagonals(size, matrix, low_limit_center)

        fill_center(size, matrix)   
        
        print_matrix(size, matrix)

        
    except EOFError:
        break
