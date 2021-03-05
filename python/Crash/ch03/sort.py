from random import randint

# Construct a list of 10 random integer values between 0 and 100.
values = []
for i in range(0, 10):
    values.append(randint(0, 100));
print(f"{len(values)}: {values}")

# Reverse in place.
values.reverse()
print(values)

# Sort but do not change.
print(sorted(values))
print(values)

# Sort in reverse order but do not change.
print(sorted(values, reverse=True))
print(values)

# Sort in place.
values.sort()
print(values)
