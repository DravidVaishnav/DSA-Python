# find the only number in list which appears odd number of times

# through iteration
def odd_num(lst):

    for i in range(len(lst)):
        count = 0
        for j in range(len(lst)):
            if lst[i] == lst[j]:
                count += 1
        if count % 2 != 0:
            return lst[i]

# using count method
def oddnum(lst):

    for x in lst:
        count = lst.count(x)
        if count%2 != 0:
            return x
        
# using XOR
def odd_num_opt(lst):

    res = 0
    for x in lst:
        res = res ^ x
    return res

l1 = [1,1,1,2,2,4,3,4,3]
print(odd_num(l1))
print(oddnum(l1))
print(odd_num_opt(l1))

