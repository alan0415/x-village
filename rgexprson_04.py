import re

text = "cookie and cake"

pattern = r'cookie'

def repl(match):
    new_string = match.group()+ '-' +match.group()
    return new_string

new_text = re.sub(pattern, repl, text)

print("Orignal text:",text)
print("After substitution:",new_text)