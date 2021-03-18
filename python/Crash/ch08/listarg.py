numbers = [i for i in range(10)]


# Square all of the numbers.
def square(values):
    for i, v in enumerate(values):
        values[i] = v * v
    print(values)


# Pass a copy.
square(numbers[:])
print(numbers)

# Pass the original.
square(numbers)
print(numbers)
