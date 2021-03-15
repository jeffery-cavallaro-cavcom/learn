x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

if x < y:
    print(f"{x} < {y}: {x < y}")
if x <= y:
    print(f"{x} <= {y}: {x <= y}")
if x == y:
    print(f"{x} == {y}: {x == y}")
if x != y:
    print(f"{x} != {y}: {x != y}")
if x >= y:
    print(f"{x} >= {y}: {x >= y}")
if x > y:
    print(f"{x} > {y}: {x > y}")

if x < 0 and y < 0:
    print("Both values are negative")
if x < 0 or y < 0:
    print("At least one value is negative")

if x in range(10):
    print(f"0 <= {x} < 10")
if y not in range(10):
    print(f"{y} < 0 or {y} >= 10")

fruit = ['apple', 'orange', 'banana', 'mango', 'strawberry']
f = 'banana'
if f in fruit:
    print(f"{f} is a known fruit")
f = 'tomato'
if f not in fruit:
    print(f"{f} is not a known fruit")
