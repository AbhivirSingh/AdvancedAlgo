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
