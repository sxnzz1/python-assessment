rmv = input("Enter a string:")
result = ""

for character in rmv:
    if not character.islower():
        result += character
print("removed letter :", result)
