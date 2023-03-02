# left rotate given list by one

def left_rotate(lst):
    
    new = lst[1:] + lst[0:1]
    return new

print(left_rotate([1,2,3,4]))

def left_rotate_append(lst):

    lst.append(lst.pop(0))
    return lst

print(left_rotate_append([5,6,7,8]))

def left_rotate_iter(lst):

    new = []

    for i in range(len(lst)-1):
        new.append(lst[i+1])
    new.append(lst[0])

    return new

print(left_rotate_iter([4,6,8,10]))