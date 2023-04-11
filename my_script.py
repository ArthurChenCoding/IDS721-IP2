def reverse_string(string):
    return string[::-1]

user_input = input("Enter a string to reverse: ")

reversed_string = reverse_string(user_input)

print("Reversed string:", reversed_string)
