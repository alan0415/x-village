#solve it
import re

a = input("Enter a name:")
b = input("Enetr a name:")
c = input("Enetr a name:")
text = a
text2 = b
text3 = c

pattern = r'(?P<lastname>\w\w\w\w) (?P<firstname>\w\w\w)'

match = re.search(pattern, text)
match2 = re.search(pattern, text2)
match3 = re.search(pattern, text3)

if match is not None:
    print(str(a) + ":" + match.groupdict())
    print(b + ":" + match2.groupdict())
    print(c + ":" + match3.groupdict())