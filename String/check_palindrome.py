# check whether a string is palindrome or not

def check_palindrome(str):

    low = 0 # setting low var that checks from left side of string
    high = len(str)-1 # setting high var that checks from right side of string

    while low<high:

        if str[low]!=str[high]: # if low and high are not same, string not palindrome hence return
            return False
            break
        low=low+1
        high=high-1
    else:
        return True # string is palindrome
    
def slice_palindrome(str):

    return str == str[::-1] # reversing string then comparing with original
    


print(check_palindrome('hello'))
print(check_palindrome('malayalam'))
print(slice_palindrome('madam'))



