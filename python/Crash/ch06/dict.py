def valuer(orig):
    try:
        actual = int(orig)
    except ValueError:
        pass
    else:
        return actual

    try:
        actual = float(orig)
    except ValueError:
        pass
    else:
        return actual

    low = orig.lower()
    if low in ['true', 'on', 'yes']:
        return True
    if low in ['false', 'off', 'no']:
        return False

    if not orig:
        return None

    return orig


table = {}

while True:
    key = None
    value = None
    try:
        key = valuer(input("key: "))
        value = valuer(input("value: "))
    except KeyboardInterrupt or EOFError:
        break
    table[key] = value
    print(table)
