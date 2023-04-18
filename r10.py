def sum_of_divisors(num):
    """
    Returns the sum of all divisors of a number.
    """
    divisors_sum = 0
    for i in range(1, num+1):
        if num % i == 0:
            divisors_sum += i
    return divisors_sum

# Example usage
num = 9
print("The sum of all divisors of", num, "is", sum_of_divisors(num))
