# 03.08.2017
# importing an entire module
import classes_module

my_beetle = classes_module.Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())

my_tesla = classes_module.ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())
