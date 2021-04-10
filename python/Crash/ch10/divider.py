while True:
    try:
        values = [int(i) for i in input('Enter two integers: ').split()]
        print(values[0]/values[1])
    except (EOFError, KeyboardInterrupt):
        print()
        break
    except ZeroDivisionError:
        print("Cannot divide by 0!")
    except ValueError:
        print("Invalid input value!")
