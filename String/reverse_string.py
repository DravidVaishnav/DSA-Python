# reverse the given string

def rev_str_iter(str):
# strings in python are immutable, hence we create another rev str
    rev = ""
    for i in str:
        rev = i + rev

    return rev

def rev_str(str):
# using string slicing
    return str[::-1]

print(rev_str('helloworld'))
print(rev_str_iter('helloworld'))
