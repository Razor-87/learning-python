def make_car(brand, model, **other):
    """Saves information about the machine in the dictionary."""
    info_car = {}
    info_car['brand'] = brand
    info_car['model'] = model
    for key, value in other.items():
        info_car[key] = value
    return info_car


car = make_car('Toyota', 'Sprinter Trueno', code='AE86', engine='1.6L')
print(car)
