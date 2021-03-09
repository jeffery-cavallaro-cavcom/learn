from random import randint

numbers = [randint(0, 100) for i in range(10)]

print(sorted(numbers))
print(f"Min: {min(numbers)}")
print(f"Max: {max(numbers)}")
print(f"Sum: {sum(numbers)}")

numbers.sort()
print(numbers[5:])
print(numbers[5:9])
print(numbers[5:])
print(numbers[:])

same = numbers
diff = numbers[:]
same.append(42)
diff.append(-1)
print(numbers)
print(same)
print(diff)