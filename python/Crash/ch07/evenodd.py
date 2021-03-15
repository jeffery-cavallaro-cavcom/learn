more = True
while more:
    value = None
    try:
        value = int(input("next value> "))
    except ValueError:
        more = False
    else:
        print(f"{value} is {'odd' if value % 2 else 'even'}")
