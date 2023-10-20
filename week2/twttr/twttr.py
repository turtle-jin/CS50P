

prompt = input("Input: ")
str = ""
char_to_remove = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
for char in prompt:
    if char not in char_to_remove:
        str += char
print(f"Output: {str}")