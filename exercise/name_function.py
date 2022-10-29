def get_formatted_name_(first, last, middle=''):
    """Generate a neatly formatted full name."""
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()


def get_formatted_name(first, middle, last): 
    """Gera um nome completo formatado de modo elegante."""
    full_name = first + ' ' + middle + ' ' + last 
    return full_name.title()
