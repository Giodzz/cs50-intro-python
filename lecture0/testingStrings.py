#Ask for user name
name = input("What's your name? ")

# Remove whitespace from str (begginig and end)
name = name.strip() 

# Capitalize user's name (only first letter)
name = name.capitalize()

name = name.title()

#Say hello to user
print(f"Hello, {name}!")