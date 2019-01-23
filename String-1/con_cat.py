'''Given two strings, append them together (known as "concatenation") and return the result. 
However, if the concatenation creates a double-char, then omit one of the chars, 
so "abc" and "cat" yields "abcat".'''

def con_cat(str1, str2):
    if len(str1) == 0 or len(str2) == 0:
        return str1 + str2
    return str1 + str2 if str1[-1] != str2[0] else str1[:-1] + str2