def make_shirt(size, text):
    """Size and text on the shirt."""
    print("\nSize: " + size.upper())
    print("Text: " + text)


make_shirt('xxl', 'Hello World')
make_shirt(text='i love dicts', size='xl')


def make_shirt_2(size='l', text='I love Python'):
    """Size and text on the shirt."""
    print("\nSize: " + size.upper())
    print("Text: " + text)


make_shirt_2()
make_shirt_2(text='I love dicts', size='xl')


def describe_city(city, country='russia'):
    """Displays the city and country."""
    print("\n" + city.title() + " is in " + country.title())


describe_city('moscow')
describe_city('saint petersburg')
describe_city('tokyo', 'japan')
