# check whether a list is sorted or not

# through iteration
def check_sorted(lst):

    if len(lst)<=1:
        return True

    for i in range(len(lst)-1):
        if lst[i] > lst[i+1]:
            return False 
    return True

# using sorted func
def issorted(lst):

    l = sorted(lst)
    if l == lst:
        return True
    else:
        return False

l1 = [234,12,56,12,45]
l2 = [12,23,56,67]

print(check_sorted(l1))
print(check_sorted(l2))
print(issorted(l1))
print(issorted(l2))
