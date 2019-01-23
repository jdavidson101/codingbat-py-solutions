'''Given a string, return true if the string starts with "hi" and false otherwise.'''

def start_hi(str):
    return str[0:2] == "hi"

''' codingbat test cases
"hi there", True
"hi", True
"hello hi", False
"", False
"h", False
"Hi", False
" hi", False
"there hi", False
'''

#difficulty:145
