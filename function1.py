def in_range(number, start, end):
    return start <= number <= end
# Check if 5 is in the range from 0 to 10
print(in_range(5, 0, 10))  # Output: True

# Check if 15 is in the range from 0 to 10
print(in_range(15, 0, 10))  # Output: False

# Check if 0 is in the range from -10 to 10
print(in_range(0, -10, 10))  # Output: True

# Check if -15 is in the range from -10 to 10
print(in_range(-15, -10, 10))  # Output: False
