lst = [12,55,99,77,4641,2,7,6]

smallest = float('inf')
secondSmall = float('inf')

for num in lst:
    if num < smallest:
        secondSmall = smallest
        smallest = num
    elif num < secondSmall and num != smallest:
        secondSmall = num
print("second smallest num is:  ",secondSmall)
