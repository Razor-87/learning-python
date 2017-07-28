# 28.07.2017
import exercise_module_functions_2

car = exercise_module_functions_2.make_car('Toyota',
                                           'Sprinter Trueno',
                                           code='AE86', engine='1.6L')
print(car)


"""
import exercise_module_functions_2 as emf2

car = emf2.make_car('Toyota',
                    'Sprinter Trueno',
                    code='AE86', engine='1.6L')
print(car)
"""

"""
from exercise_module_functions_2 import make_car

car = make_car('Toyota',
               'Sprinter Trueno',
               code='AE86', engine='1.6L')
print(car)
"""

"""
from exercise_module_functions_2 import make_car as mc

car = mc('Toyota',
         'Sprinter Trueno',
         code='AE86', engine='1.6L')
print(car)
"""

"""
from exercise_module_functions_2 import *

car = make_car('Toyota',
               'Sprinter Trueno',
               code='AE86', engine='1.6L')
print(car)
"""
