import numpy as np
import time

def empirical_analysis():
    sizes = [128, 256, 512, 1024, 2048]  # Example sizes for matrices or number of digits
    
    print("Empirical Analysis of Karatsuba and Strassen's Algorithms")

    # Performance of Karatsuba Multiplication
    for n in sizes:
        x = np.random.randint(10**n)
        y = np.random.randint(10**n)
        
        # Traditional multiplication
        start = time.time()
        traditional_result = traditional_multiplication(x, y)
        traditional_time = time.time() - start
        
        # Karatsuba multiplication
        start = time.time()
        karatsuba_result = karatsuba(x, y)
        karatsuba_time = time.time() - start
        
        print(f"Number Size: {n} digits")
        print(f"Traditional Multiplication Time: {traditional_time:.6f} seconds")
        print(f"Karatsuba Multiplication Time: {karatsuba_time:.6f} seconds\n")
    
    # Performance of Strassen Matrix Multiplication
    for n in sizes:
        A = np.random.randint(10, size=(n, n))
        B = np.random.randint(10, size=(n, n))
        
        # Traditional matrix multiplication
        start = time.time()
        traditional_matrix_result = traditional_matrix_multiplication(A, B)
        traditional_matrix_time = time.time() - start
        
        # Strassen matrix multiplication
        start = time.time()
        strassen_matrix_result = strassen(A, B)
        strassen_matrix_time = time.time() - start
        
        print(f"Matrix Size: {n}x{n}")
        print(f"Traditional Matrix Multiplication Time: {traditional_matrix_time:.6f} seconds")
        print(f"Strassen Matrix Multiplication Time: {strassen_matrix_time:.6f} seconds\n")

# Run the empirical analysis
empirical_analysis()
