'''Given a string, return a version without the first 2 chars. 
Except keep the first char if it is 'a' and keep the second char if it is 'b'. 
The string may be any length. Harder than it looks.'''

def de_front(str):
    str += "  "
    if str[0] == 'a' or str[1] == 'b':
        if str[0] == 'a':
            if str[1] == 'b':
                return str[:-2]
            return str[0] + str[2:-2]
        return str[1:-2]
    return str[2:-2]