def is_perfect_number(n):
    # Check if n is a positive integer
    if not isinstance(n, int) or n < 1:
        return False
    
    # Find the divisors of n
    divisors = []
    for i in range(1, n):
        if n % i == 0:
            divisors.append(i)
    
    # Check if the sum of the divisors is equal to n
    return sum(divisors) == n

# Check if 6 is a perfect number
print(is_perfect_number(6))  # Output: True

# Check if 28 is a perfect number
print(is_perfect_number(28))  # Output: True

# Check if 12 is a perfect number
print(is_perfect_number(12))  # Output: False
