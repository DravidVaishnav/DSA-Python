# largest number in list

def largest(lst):

    if not lst:
        return None
    else:
        max_num = lst[0]
        for x in lst:
            if x > max_num:
                max_num = x

        return max_num

l1=[1,2,3,4,5]
print(largest(l1))

# second largest

def second_largest(lst):

    if len(lst)>1:
        return lst[::-1][1]
    else:
        return None
    
print(second_largest(l1))
print(second_largest([1]))
