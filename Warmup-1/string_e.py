#Return true if the given string contains between 1 and 3 'e' chars.

def string_e(str):
    count = str.count('e')
    return count >= 1 and count <= 3

''' codingbat test cases
"Hello", True
"Heelle", True
"Heelele", False
"", False
"e", True
"hE", False
"hehehe", True
"beeeeat", False
"eeeeeeee", False
"EeEe", True
'''

#difficulty:181
