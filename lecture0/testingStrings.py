#Ask for user name
name = input("What's your name? ")

# Remove whitespace from str (begginig and end)
name = name.strip() 

# Capitalize user's name (only first letter)
name = name.capitalize()
name = name.title()

# we can chain these methods
name = name.strip().title()

# Split user's name into first name and last name
first, last = name.split(' ')

#Say hello to user
print(f"Hello, {first}!")