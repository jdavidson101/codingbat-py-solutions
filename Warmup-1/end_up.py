# Given a string, return a new string where the last 3 chars are now in upper case. 
# If the string has less than 3 chars, uppercase whatever is there. Note that str.upper() returns the uppercase version of a string.

def end_up(str):
    if len(str) > 3:
        return str[:len(str) - 3] + str[len(str) - 3:].upper()
    return str.upper()