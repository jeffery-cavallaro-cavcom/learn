numbers = set()

while True:
    value = None
    try:
        value = int(input("next> "))
    except ValueError:
        break
    numbers.add(value)
    print(numbers)
