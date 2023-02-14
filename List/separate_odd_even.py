# we want to separate odd and even numbers from a given list

def odd_even(lst):

    odd = []
    even = []

    for i in lst:

        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)

    return even,odd

even_lst,odd_lst = odd_even([1,2,3,4,5])
print(even_lst)
print(odd_lst)