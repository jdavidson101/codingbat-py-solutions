'''Given a string, take the last char and return a new string with the last char added at the front and back, 
so "cat" yields "tcatt". The original string will be length 1 or more.'''

def back_around(str):
    if len(str) > 0:
        str = str[len(str) - 1] + str + str[len(str) - 1]
    return str