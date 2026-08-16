string = "one,two,three,four,five"
delimiters = [","]
for d in delimiters[1:]:
    string = text.replace(d, delimiters)
result = string.split(delimiters[0])
print(result)
