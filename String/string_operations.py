# basic string operations

# checking for substring

s1 = 'helloworld'
s2 = 'hello'

print(s2 in s1)
print(s2 not in s1)

# checking for position 

s3 = 'geeksforgeeks'
s4 = 'geeks'

print(s3.index(s4)) # returns index of first occurence 
print(s3.rindex(s4)) # returns index of last occurence
print(s3.index(s4,1,13)) # returns index of first occurence in given range

# string methods

u = s1.upper() # converts string in uppercase
l = u.lower() # converts string in lowercase

print(u)
print(l)

print(u.islower()) # checks whether string is lowercase
print(u.isupper()) # checks whether string is uppercase

print(s3.startswith(s4)) # checks whether string starts with given substring
print(s3.endswith(s4)) # checks whether string ends with given substring


# split -> used to split string , join -> used to join strings to form one string
s5 = 'hello world python'
print(s5.split()) # splits based on spaces

s6 = 'hello,world,python'
print(s6.split(',')) # splits based on ,

x = ['hello','world','python']
print(" ".join(x)) # joins elements of list with space
print(", ".join(x)) # joins elements of list with ,space


# strip -> used for removing unwanted spaces and characters , by default strips spaces
s7 = '  helloworld  '
print(s7.strip()) # removes spaces around corners
print(s7.lstrip()) # removes spaces from left side of string
print(s7.rstrip()) # removes spaces from right side of string

s8 = '--helloworld--'
print(s8.strip('-')) # removes - from both sides
print(s8.lstrip('-')) # removes - from left side
print(s8.rstrip('-')) # removes - from right side

# find -> finds index of substring, similar to index method but
# index method throws error if substring is not found but 
# find returns -1 instead

print(s3.find(s4))
print(s3.find('hi')) # substring not present hence returns -1