# list comprehension

def odd_even(lst):

    even = [x for x in lst if x%2==0]
    odd = [x for x in lst if x%2!=0]
    return even,odd

def smaller(lst,num):

    return [x for x in lst if x<num]

def character_check(full_str,short_str):

    return [x for x in full_str if x in short_str]

def initial(lst,initial):

    return [x for x in lst if x.startswith(initial)]

def uppercase(lst):

    return [x.upper() for x in lst]

def dict_reverse(d):

    return {v:k for (k,v) in d.items()}


even,odd = odd_even(list(range(1,21)))

print(even)
print(odd)
print(smaller(odd,14))
print(character_check('thankyou','abcxyz'))
print(uppercase(initial(['darthvader','master','stormtrooper'],'d')))

# set comprehension

l1 = [12,14,10,12,23,14]

st = {x for x in l1 if x%2==0}

print(st)

# dictionary comprehension

dt = {f'sqrt of {x}': x**0.5 for x in st}
print(dt)

# zip

f1 = [7,10,21]
f2 = ['Ronaldo','Messi','Asensio']

print(list(zip(f1,f2)))
d = dict(zip(f1,f2))
print(d)
print(dict_reverse(d))