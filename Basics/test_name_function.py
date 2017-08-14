# 12.08.2017
def get_formatted_name(first, last, middle=''):
    """Return a full name, neatly formatted."""
    if middle:
        full_name = first + ' ' + middle + ' ' + last
    else:
        full_name = first + ' ' + last
    return full_name.title()
