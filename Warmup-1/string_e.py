#Return true if the given string contains between 1 and 3 'e' chars.

def string_e(str):
    count = str.count('e')
    return count >= 1 and count <= 3
    
