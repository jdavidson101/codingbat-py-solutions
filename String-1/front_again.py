'''Given a string, return true if the first 2 chars in the string also appear 
at the end of the string, such as with "edited".'''

def front_again(str):
    return str[:2] == str[-2:]