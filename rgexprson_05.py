import re

text = "cookie and cake"

pattern = r'cookie'

regex = re.compile(pattern)

new_text1 = regex.sub('biscuit', text)
new_text2 = re.sub(r'cookie', 'biscuit', text)

print(new_text1)
print(new_text2)