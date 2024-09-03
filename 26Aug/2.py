import time
import numpy as np

def add_matrices(A, B):
    return np.add(A, B)

def subtract_matrices(A, B):
    return np.subtract(A, B)

def strassen(A, B):
    n = len(A)

    if n == 1:
        return A * B

    # Divide the matrices into quadrants
    mid = n // 2
    A11, A12, A21, A22 = A[:mid, :mid], A[:mid, mid:], A[mid:, :mid], A[mid:, mid:]
    B11, B12, B21, B22 = B[:mid, :mid], B[:mid, mid:], B[mid:, :mid], B[mid:, mid:]

    # Conquer: Calculate the 7 products using the formulas
    M1 = strassen(add_matrices(A11, A22), add_matrices(B11, B22))
    M2 = strassen(add_matrices(A21, A22), B11)
    M3 = strassen(A11, subtract_matrices(B12, B22))
    M4 = strassen(A22, subtract_matrices(B21, B11))
    M5 = strassen(add_matrices(A11, A12), B22)
    M6 = strassen(subtract_matrices(A21, A11), add_matrices(B11, B12))
    M7 = strassen(subtract_matrices(A12, 
    
    A22), add_matrices(B21, B22))

    # Combine the results
    C11 = M1 + M4 - M5 + M7
    C12 = M3 + M5
    C21 = M2 + M4
    C22 = M1 - M2 + M3 + M6

    # Combine quadrants into a full matrix
    C = np.zeros((n, n))
    C[:mid, :mid], C[:mid, mid:], C[mid:, :mid], C[mid:, mid:] = C11, C12, C21, C22

    return C

# Traditional O(n^3) matrix multiplication for comparison
def traditional_matrix_multiplication(A, B):
    return np.dot(A, B)



def compare_matrix_multiplication_performance(A, B):
    # Traditional matrix multiplication
    start = time.time()
    traditional_result = traditional_matrix_multiplication(A, B)
    traditional_time = time.time() - start

    # Strassen matrix multiplication
    start = time.time()
    strassen_result = strassen(A, B)
    strassen_time = time.time() - start

    print(f"Traditional Matrix Multiplication Time: {traditional_time:.6f} seconds")
    print(f"Strassen Matrix Multiplication Time: {strassen_time:.6f} seconds")

# Example usage with large matrices
n = 4  # This can be increased for larger matrices
A = np.random.randint(10, size=(n, n))
B = np.random.randint(10, size=(n, n))

compare_matrix_multiplication_performance(A, B)
