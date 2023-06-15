#Ask for user name
name = input("What's your name? ")

# Remove whitespace from str (begginig and end)
name = name.strip() 

#Capitalize user's name
name = name.capitalize()

#Say hello to user
print(f"Hello, {name}!")