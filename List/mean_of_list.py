# we want to find mean of all elements in list

def average(lst):

    n = len(lst)
    sum = 0

    for i in lst:
        sum+=i

    avg = sum/n

    return avg

def average_opt(lst):

    return sum(lst)/len(lst)

print(average([3,6,4]))
print(average_opt([3,6,4]))


