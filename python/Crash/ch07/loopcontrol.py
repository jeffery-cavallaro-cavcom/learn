for i in range(10):
    if i % 2:
        # Ignore odd values.
        continue
    if i == 8:
        # Stop at 8.
        break
    print(i)
