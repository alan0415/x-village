import re

text1 = "and cookie"
text2 = "CakeCakeCake and cookie"

plus_pattern = "(Cake)+ and cookie"# 要match 一個或多個cake,再加上'and cookie'

plus_match1 = re.search(plus_pattern, text1)
plus_match2 = re.search(plus_pattern, text2)

print(plus_match1)
print(plus_match2.group())