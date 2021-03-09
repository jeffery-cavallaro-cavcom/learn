# A simple range from 0 to n-1.
for i in range(10):
    if i > 0:
        print(' ', end='')
    print(i, end='')
print()

# A range from n to m-1.
for i in range(3, 10):
    if i > 3:
        print(' ', end='')
    print(i, end='')
print()

# A range from n to m-1, every 2.
for i in range(0, 10, 2):
    if i > 0:
        print(' ', end='')
    print(i, end='')
print()

# Converting a range to a list.
print(list(range(10, 0, -3)))

# Squares.
squares = []
for i in range(11):
    squares.append(i*i)
print(squares)
