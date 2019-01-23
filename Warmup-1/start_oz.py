# Given a string, return a string made of the first 2 chars (if present), 
# however include first char only if it is 'o' and include the second only if it is 'z', so "ozymandias" yields "oz".

def start_oz(str):
    if len(str) > 1 and str[0] == 'o':
        return 'oz' if str[1] == 'z' else 'o'
    return str[:2]

''' codingbat test cases
"ozymandias", "oz"
"bzoo", "z"
"oxx", "o"
"", ""
"h", "h"
"oz", "oz"
"of", "o"
"oz the wizard", "oz"
" hi", " h"
"Of", "Of"
"oZ", "o"
'''

#difficulty:166