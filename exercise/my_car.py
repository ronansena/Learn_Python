from car import Car
from car import ElectricCar


my_used_car = Car('subaru', 'outback', 2013)
my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 23
my_new_car.update_odometer(20) #Modificando o valor de um atributo com um método
my_used_car.increment_odometer(100)  #Incrementando o valor de um atributo com um método
my_new_car.read_odometer() 
my_used_car.read_odometer()

my_tesla = ElectricCar('tesla', 'model s', 2016)

print(my_tesla.get_descriptive_name()) 
#print(my_tesla.describe_battery())
print(my_tesla.battery.describe_battery()) #Instâncias como atributos
print(my_tesla.fill_gas_tank())
print(my_tesla.battery.get_range())