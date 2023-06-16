# By default input is a str -> so it concatenates
x = input("What's x? ")
y = input("What's y? ")

# transforming str to int to actually sum the numbers
z = int(x) + int(y)
print(z)

# or nest functions
x = float(input("x: "))
y = float(input("y: "))
print(f"{round(x+y):,}")
print(f"{x/y:.2f}")
