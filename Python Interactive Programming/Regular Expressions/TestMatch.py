import re

pattern = r"Cookie"
sequence = "Cookie"

def TestMatch (pattern, sequence):
    if re.match(pattern, sequence):
        print("Match!")
    else: print("Not a match!")


TestMatch(pattern, sequence)
