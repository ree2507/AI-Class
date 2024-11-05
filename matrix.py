# pake library
import numpy as np

A = np.array([[3, 0], [1, -2], [1, 1]])
B = np.array([[4, -1], [0, 2]])
C = np.array([[1, 4, 2], [3, 1, 5]])
D = np.array([[1, 5, 2], [-1, 0, 1], [3, 2, 4]])
E = np.array([[6, 1, 3], [-1, 2, 2], [4, 1, 3]])


def multiply_matrices(X, Y):
    result = np.zeros((X.shape[0], Y.shape[1])) 
    for i in range(X.shape[0]):  
        for j in range(Y.shape[1]): 
            for k in range(Y.shape[0]):  
                result[i, j] += X[i, k] * Y[k, j]
    return result

def add_matrices(X, Y):
    result = np.zeros(X.shape)  
    for i in range(X.shape[0]):
        for j in range(X.shape[1]):
            result[i, j] = X[i, j] + Y[i, j]
    return result


def subtract_matrices(X, Y):
    result = np.zeros(X.shape)  
    for i in range(X.shape[0]):
        for j in range(X.shape[1]):
            result[i, j] = X[i, j] - Y[i, j]
    return result


try:
    AC = multiply_matrices(A, C)
    print("Hasil A x C:")
    for row in AC:
        print(row)
except ValueError as e:
    print("Error saat menghitung A x C:", e)


try:
    AD = multiply_matrices(A, D)
    print("\nHasil A x D:")
    for row in AD:
        print(row)
except ValueError as e:
    print("\nError saat menghitung A x D:", e)


try:
    DE_add = add_matrices(D, E)
    print("\nHasil D + E:")
    for row in DE_add:
        print(row)
except ValueError as e:
    print("\nError saat menghitung D + E:", e)


try:
    DE_sub = subtract_matrices(D, E)
    print("\nHasil D - E:")
    for row in DE_sub:
        print(row)
except ValueError as e:
    print("\nError saat menghitung D - E:", e)


# tanpa library
A = [[3, 0], [1, -2], [1, 1]]
B = [[4, -1], [0, 2]]
C = [[1, 4, 2], [3, 1, 5]]
D = [[1, 5, 2], [-1, 0, 1], [3, 2, 4]]
E = [[6, 1, 3], [-1, 2, 2], [4, 1, 3]]


def multiply_matrices(X, Y):
    
    result = [[0 for _ in range(len(Y[0]))] for _ in range(len(X))]
    for i in range(len(X)):  
        for j in range(len(Y[0])):  
            for k in range(len(Y)):  
                result[i][j] += X[i][k] * Y[k][j]
    return result


def add_matrices(X, Y):
    result = [[0 for _ in range(len(X[0]))] for _ in range(len(X))]  
    for i in range(len(X)):
        for j in range(len(X[0])):
            result[i][j] = X[i][j] + Y[i][j]
    return result


def subtract_matrices(X, Y):
    result = [[0 for _ in range(len(X[0]))] for _ in range(len(X))]  
    for i in range(len(X)):
        for j in range(len(X[0])):
            result[i][j] = X[i][j] - Y[i][j]
    return result


try:
    AC = multiply_matrices(A, C)
    print("Hasil A x C:")
    for row in AC:
        print(row)
except ValueError as e:
    print("Error saat menghitung A x C:", e)


try:
    AD = multiply_matrices(A, D)
    print("\nHasil A x D:")
    for row in AD:
        print(row)
except ValueError as e:
    print("\nError saat menghitung A x D:", e)

try:
    DE_add = add_matrices(D, E)
    print("\nHasil D + E:")
    for row in DE_add:
        print(row)
except ValueError as e:
    print("\nError saat menghitung D + E:", e)


try:
    DE_sub = subtract_matrices(D, E)
    print("\nHasil D - E:")
    for row in DE_sub:
        print(row)
except ValueError as e:
    print("\nError saat menghitung D - E:", e)