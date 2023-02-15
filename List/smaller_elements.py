# given input number x and list we need to return list containing numbers less than x

def smaller(lst,x):

    small = []

    for i in lst:
        if i < x:
            small.append(i)

    return small

l = [34,23,12,65,30]
x = 30

print(smaller(l,x))

