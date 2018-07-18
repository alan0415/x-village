import re

text = "Today is good day to learn regular expression."

pattern = r'regular expression'

match = re.search(pattern, text)

start_index = match.span()[0]
end_index = match.span()[1]
match_starting = match.group()
print("The location of '{}' is between {} and {} in text.".format(match_starting, start_index, end_index))