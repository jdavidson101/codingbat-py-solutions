'''Given a string, return true if "bad" appears starting at index 0 or 1 in the string,
 such as with "badxxx" or "xbadxx" but not "xxbadxx". The string may be any length, 
 including 0. Note: use .equals() to compare 2 strings.'''

def has_bad(str):
    return str[:3] == 'bad' or str[1:4] == 'bad'

