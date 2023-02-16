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

# this func takes 2 iterations
def second_largest(lst):

    lar = largest(lst)
    sec_lar = None

    if len(lst)<=1:
        return None

    for x in lst:
        if x != lar:
            if sec_lar == None:
                sec_lar = x
            else:
                sec_lar = max(sec_lar,x)

    return sec_lar


# this func takes only one iteration
def second_largest_opt(lst):

    if len(lst)<=1:
        return None
    
    lar = lst[0]
    sec_lar = None
    
    for x in lst[1:]:

        if x > lar:
            sec_lar = lar
            lar = x
        elif x != lar:
            if sec_lar == None or sec_lar < x:
                sec_lar = x
    return sec_lar

    
print(second_largest(l1))
print(second_largest([1]))
print(second_largest_opt(l1))
