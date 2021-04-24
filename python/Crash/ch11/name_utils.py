def get_formatted_name(last, first, middle=None):
    """ Constructs a full name in title case """
    name = first
    if middle:
        name = f"{name} {middle}"
    name = f"{name} {last}"
    return name.title()
