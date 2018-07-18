import re

text1 = "cake and cookie"
text2 = "cookie and cake"

pattern = "cookie"

match1 = re.match(pattern, text1)
match2 = re.match(pattern,text2)

print("Type of 'match1 ' object:", type(match1))
print(match1)
print("="*50)
print("Type of 'match2' object:", type(match2))
print("Matching pattern: %r" % match2.group())