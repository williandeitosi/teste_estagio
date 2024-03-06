def reverse_string(s):
    reversed_string = ""
    for char in s:
        reversed_string = char + reversed_string
    return reversed_string


strings = ["willian", "Hello, World!", "palindromo", "civic"]
for s in strings:
    print(f"String Original: {s}")
    print(f"String Invertida: {reverse_string(s)}")
