# comparison of strings 
# string comparison , compares unicode values for respective string indices
# ord(char) -> used to get unicode of char
# chr(unicode value) -> used to get char for given unicide
# Unicode values : a to z -> 97 to 122, A to Z -> 65 to 90

s1 = 'helloworld'
s2 = 'abc'
s3 = 'abcd'
s4 = 'ABCD'

print(chr(100))
print(ord('a'))
print(ord('h'))
print(ord('A'))

print(s2<s1) # ord('a') -> 97 < ord('h') -> 104
print(s2>s1)

print(s2<s3) # 'abc' and 'abcd' have 3 characters equal and s3 has one extra char hence greater
print(s2!=s3) 

print(s3<s4) # ord('a') -> 97 > ord('A')-> 65 hence s3 is greater
print(s3==s4) 