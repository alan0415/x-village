import re

text = 'cake and cookie'

pattern = r'(cake) and (cookie)'

match = re.search(pattern, text)

print("Group1 matching strating:", match.group(1))
print("Group2 matching starting:", match.group(2))

print("Group1 and Group2 matching string:", match.group(1,2))