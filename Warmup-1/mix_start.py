'''Return true if the given string begins with "mix", except the 'm' can be anything, so "pix", "9ix" .. all count.'''

def mix_start(str):
    return str[1:3] == "ix"

''' codingbat test cases
"mix snacks", True
"pix snacks", True
"piz snacks", False
"", False
"m", False
"cat", False
"mix", True
"zixa", True
"MIX", False
"5ix", True
"dmixog", False
"&ix*&(", True
"dogxix", False
'''

#difficulty: 163
