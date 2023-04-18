import random

my_range = range(1, 11)
my_list = list(my_range)
random_item = random.choice(my_list)
print(random_item)


# first convert the range object to a list or tuple, and then use the random.choice() function.