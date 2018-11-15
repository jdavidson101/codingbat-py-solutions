'''Return true if the given string begins with "mix", except the 'm' can be anything, so "pix", "9ix" .. all count.'''

def mix_start(str):
    return str[1:3] == "ix"