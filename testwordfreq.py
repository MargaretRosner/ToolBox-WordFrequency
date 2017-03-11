import string
lines = "a.$%bgtr"

for c in lines:
    if c in set(string.punctuation):
        lines = lines.replace(c,"")
print(lines)
