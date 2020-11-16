import re

input = r'Co\wk\we'
desirable = 'Cookie'

def TestSearch(input, desirable):
    val = re.search(input, desirable).group()
    return val

print(TestSearch(input, desirable))
