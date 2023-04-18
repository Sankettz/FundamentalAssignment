lst = [1,2,3,4,5,6,7,8,9,111]
sublst = [1,2,3,4]
n = len(sublst)
any((sublst == lst[i:i+n]) for i in range(len(lst)-n+1))
print(sublst)