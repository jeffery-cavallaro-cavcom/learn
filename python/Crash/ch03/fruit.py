# A list with all the same type.
fruit = ["apple", "orange", "pineapple", "grape", "mango", "strawberry", "banana"]

for i, f in enumerate(fruit):
    print(f"fruit[{i}] = {f.title()}")

print(fruit[0])
print(fruit[-1])
print(fruit[1:3])
print(fruit[:3])
print(fruit[1:])

# A list with different types.
data = [42, True, 'hello', 3.14, None, [1, 2, 3]]

for i, d in enumerate(data):
    print(f"data[{i}] = {d}")

print(fruit)
fruit.append('tomato')
print(fruit)
fruit.insert(1, "grapefruit")
print(fruit)
fruit.remove("apple")
print(fruit)
fruit += ["blackberry", "blueberry", "apple"]
print(fruit)
del fruit[4]
print(fruit)
print(fruit.pop())
print(fruit.pop(2))
print(fruit)
fruit[3] = "apple"
print(f"{len(fruit)}: {fruit}")
