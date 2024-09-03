import time
def karatsuba(x, y):
    # Base case for the recursion
    if x < 10 or y < 10:
        return x * y
    
    # Calculate the size of the numbers
    n = max(len(str(x)), len(str(y)))
    m = n // 2
    
    # Split the numbers
    x1 = x // 10**m
    x0 = x % 10**m
    y1 = y // 10**m
    y0 = y % 10**m
    
    # Recursively calculate the three products
    P1 = karatsuba(x1, y1)
    P2 = karatsuba(x0, y0)
    P3 = karatsuba(x1 + x0, y1 + y0)
    
    # Calculate the cross-term
    P4 = P3 - P1 - P2
    
    # Combine the results
    result = P1 * 10**(2*m) + P4 * 10**m + P2
    
    return result

# Traditional O(n^2) multiplication for comparison
def traditional_multiplication(x, y):
    return x * y

def compare_performance(x, y):
    # Traditional multiplication
    start = time.time()
    traditional_result = traditional_multiplication(x, y)
    traditional_time = time.time() - start

    # Karatsuba multiplication
    start = time.time()
    karatsuba_result = karatsuba(x, y)
    karatsuba_time = time.time() - start

    print(f"Traditional Multiplication Result: {traditional_result}")
    print(f"Karatsuba Multiplication Result: {karatsuba_result}")
    print(f"Traditional Multiplication Time: {traditional_time:.6f} seconds")
    print(f"Karatsuba Multiplication Time: {karatsuba_time:.6f} seconds")

# Example usage with large numbers
x = 123456789012345678901234567890
y = 987654321098765432109876543210

compare_performance(x, y)
