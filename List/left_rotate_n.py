# left rotate given list by n times
def left_rotate(lst,n):

    return lst[n:] + lst[:n]

print(left_rotate([1,2,3,4],2))

def left_rotate_append(lst,n):

    for i in range(n):
        lst.append(lst.pop(0))

    return lst

print(left_rotate_append([1,2,3,4],3))

def left_rotate_iter(lst,n):

    new = []
    length = len(lst)
    for i in range(length):
        if i+n>length-1:
            j = i + n -length
        else:
            j = i + n
        new.append(lst[j])
    
    return new

print(left_rotate([12,13,14,15],2))