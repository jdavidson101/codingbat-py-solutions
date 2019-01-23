'''Given a string, take the first 2 chars and return the string with the 2 chars added at both the front and back, 
so "kitten" yields"kikittenki". If the string length is less than 2, use whatever chars are there.'''

def front22(str):
    return str[:2] + str + str[:2]

''' codingbat test cases
"kitten", "kikittenki"
"Ha", "HaHaHa"
"abc", "ababcab"
"", ""
"a", "aaa"
"cat", "cacatca"
"Fa", "FaFaFa"
"sUperstitious", "sUsuperstitioussU"
"5", "555"
"cat5", "cacat5ca"
"donk3y", "dodonk3ydo"
"&", "&&&"
"dog%", "dodog%do"
"beet!e", "bebeet!ebe"
'''

#difficulty: 142