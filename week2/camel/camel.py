

user_input = input("camelCase: ")
output = ""

for char in user_input:
    if char.isupper():
        output += f"_{char.lower()}"
    else:
        output += char

print(f"snake_case: {output}")




