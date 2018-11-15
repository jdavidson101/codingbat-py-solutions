'''Given a string, if the string "del" appears starting at index 1, 
return a string where that "del" has been deleted. Otherwise, return the string unchanged.'''

def del_del(str):
    return str[0] + str[4:] if str[1:4] == 'del' else str
        