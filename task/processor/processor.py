# A basic code for matrix input from user 
R = 0
C = 0
R1 = 0
C1 = 0
import numpy as np


def zeros_matrix(rows, cols):
    M = []
    while len(M) < rows:
        M.append([])
        while len(M[-1]) < cols:
            M[-1].append(0)

    return M


def input_mat():
    matrix = []
    global R
    global C
    b = input().split(" ")
    R = int(b[0])
    C = int(b[1])
    for i in range(0, R):
        matrix.append([C for C in map(float, input().split(" "))])
    return matrix


def input_mat_int():
    matrix = []
    global R
    global C
    b = input().split(" ")
    R = int(b[0])
    C = int(b[1])
    for i in range(0, R):
        matrix.append([C for C in map(int, input().split(" "))])
    return matrix


def input_mat1():
    matrix = []
    global R1
    global C1
    b = input().split(" ")
    R1 = int(b[0])
    C1 = int(b[1])
    for i in range(0, R1):
        matrix.append([C1 for C1 in map(float, input().split(" "))])
    return matrix


def add_mat():
    m1 = input_mat()
    m2 = input_mat()
    r = [[0 for n in range(C)] for n in range(R)]
    # if len(m1) == len(m2):
    for i in range(R):
        for j in range(C):
            r[i][j] = m1[i][j] + m2[i][j]
    # else:
    # print("The operation cannot be performed.")
    # pass

    for i in range(R):
        for j in range(C):
            print(r[i][j], "", end="")
        print("")


def multiply_const():
    matrix = input_mat()
    m = int(input())

    r = [[0 for n in range(C)] for n in range(R)]

    for i in range(R):
        for j in range(C):
            r[i][j] = matrix[i][j] * m

    print_mat(r)


def multi_mat():
    mat_1 = input_mat()
    mat_2 = input_mat1()
    rowsA = len(mat_1)
    colsA = len(mat_1[0])
    rowsB = len(mat_2)
    colsB = len(mat_2[0])

    f = zeros_matrix(rowsA, colsB)

    if colsA != rowsB:
        print("The operation cannot be performed.")
        pass
    for i in range(rowsA):
        for j in range(colsB):
            total = 0
            for ii in range(colsA):
                total += mat_1[i][ii] * mat_2[ii][j]
            f[i][j] = total
    print_mat_mul(f, rowsA, colsB)


def trans_mat():
    print("1. Main diagonal")
    print("2. Side diagonal")
    print("3. Vertical line")
    print("4. Horizontal line")
    c = int(input())
    if c == 1:
        A = input_mat_int()
        B = zeros_matrix(R, C)
        for i in range(R):
            for j in range(C):
                B[i][j] = A[j][i]
        print("The result is:")
        print_mat(B)
    if c == 2:
        A = input_mat()
        A.reverse()
        B = zeros_matrix(R, C)
        for i in range(R):
            for j in range(C):
                B[i][j] = A[j][i]
        B.reverse()
        print("The result is:")
        print_mat(B)
    if c == 3:
        A = input_mat()

        for i in range(R):
            A[i].reverse()
        print("The result is:")
        print_mat(A)
    if c == 4:
        A = input_mat()
        A.reverse()

        print("The result is:")
        print_mat(A)


def mat_det():
    A = input_mat()

    n_array = np.array(A)
    det = np.linalg.det(n_array)
    print(det)


def mat_inv():
    A = input_mat()
    n_array = np.array(A)
    x_inverted = np.linalg.inv(n_array)
    print_mat(x_inverted)


def print_mat_mul(r, row, col):
    for i in range(row):
        for j in range(col):
            print(r[i][j], "", end="")
        print("")


def print_mat(r):
    for i in range(R):
        for j in range(C):
            print(r[i][j], "", end="")
        print("")


while True:
    print("1. Add matrices")
    print("2. Multiply matrix by a constant")
    print("3. Multiply matrices")
    print("4. Transpose matrix")
    print("5. Calculate a determinant")
    print("6. Inverse matrix")
    print("0. Exit")
    ch = int(input())
    if ch == 1:
        add_mat()
    elif ch == 2:
        multiply_const()
    elif ch == 3:
        multi_mat()
    elif ch == 4:
        trans_mat()
    elif ch == 5:
        mat_det()
    elif ch == 6:
        mat_inv()
    elif ch == 0:
        break
