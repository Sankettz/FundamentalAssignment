list1 = [1,2,3]
list2 = [1,22,3333]

for x,y in zip(list1,list2):
    if x!=y:
        print("lists are not equal")
    else:
        print("Lists are equal")