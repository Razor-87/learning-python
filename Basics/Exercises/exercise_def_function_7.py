def composition_sandwich(*items):
    """Displays a list of components."""
    print("\nYour sandwich consists of:")
    for item in items:
        print("- " + item.title())


composition_sandwich('bacon', 'cheese', 'sausage', 'egg')
