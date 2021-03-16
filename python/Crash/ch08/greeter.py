def greet(name):
    """
    Displays a greeting for the specified name.
    :param name: str
    :return: None
    """
    if name:
        name = name.strip().capitalize()
    if name:
        print(f"Hello, {name}!")
    else:
        print("There is no one to say hello to.")


def get_name():
    """
    Inputs a name from the standard input.
    :return: str
    """
    try:
        name = input("What is your name? ")
    except (EOFError, KeyboardInterrupt):
        name = None
    return name


greet(get_name())
