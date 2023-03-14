# search index of given pattern in string

def pattern_str(str,pattern):
    pos = str.find(pattern)

    while pos>=0:
        print(pos)
        pos = str.find(pattern,pos+1)

print(pattern_str('hello world hello','hello'))