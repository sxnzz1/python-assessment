string = "Hello (world) Python"
output = ""
rmv = 0
for i in string:
    if i == '(':
        rmv = 1
    elif i == ')':
        rmv = 0
    elif rmv == 0:
        output = output + i

print(output)
