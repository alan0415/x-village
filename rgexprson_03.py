import re

text = "cookie and cake"

pattern = r'cookie'

new_text = re.sub(pattern, 'biscuit', text)

print("Original text:", text)
print("After substitution:", new_text)
