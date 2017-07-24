# passing arguments
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')
describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster')


def describe_pet_2(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


describe_pet_2(pet_name='willie')
describe_pet_2('willie')
describe_pet_2('harry', 'willie')
describe_pet_2(animal_type='hamster', pet_name='harry')
describe_pet_2(pet_name='harry', animal_type='hamster')
