import re

text = 'cake and cookie'

pattern = r'cookie'

match = re.search(pattern, text)

print("Match starting index:", match.span()[0])
print("Match ending index:", match.span()[1])
print("Result String:", text[match.span()[0]:match.span()[1]])