'''Return true if the given non-negative number is a multiple of 3 or a multiple of 5. Use the % "mod" operator -- see Introduction to Mod'''

def or35(n):
    return n != 0 and (n % 3 == 0 or n % 5 == 0)