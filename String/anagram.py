# check whether given strings are anagrams of eachother

def anagram_sorting(str1,str2):
    # time complexity: nlog(n)
    if len(str1)!=len(str2):
        return False
    
    str1 = sorted(str1) # sort the first string
    str2 = sorted(str1) # sort the second string

    return str1 == str2 # if str1 and str2 are equal hence they are anagram

def anagram_count(str1,str2):
    # time complexity: n
    if len(str1)!=len(str2):
        return False
    count = [0] * 256 # creating list for all chars possible, initially set to zero

    for i in range(len(str1)):
        count[ord(str1[i])]+=1 # when char occurs in str1 we increment value by one
        count[ord(str2[i])]-=1 # when char occurs in str2 we decrement value by one

    for x in count:
        if x!=0:
            return False # non zero value indicates not an anagram
    return True # strings are anagram

print(anagram_sorting('bat','tab'))
print(anagram_count('bat','tab'))

