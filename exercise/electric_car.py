class Car():

    """Uma tentativa simples de representar um carro."""     

    def __init__(self, make, model, year): 
        """Inicializa os atributos que descrevem um carro."""
        self.make = make 
        self.model = model 
        self.year = year
        self.odometer_reading = 5    #Definindo um valor default para um atributo

    def get_descriptive_name(self): 
        
        """Devolve um nome descritivo, formatado de modo elegante."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model 
        return long_name.title()

    def read_odometer(self): 
        """Exibe uma frase que mostra a milhagem do carro."""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage): 
       """ Define o valor de leitura do hodômetro com o valor especificado Rejeita a alteração se for tentativa de definir um valor menor para o hodômetro """
               
       if mileage >= self.odometer_reading: 
           self.odometer_reading = mileage
       else: 
           print("You can't roll back an odometer!")             

    def increment_odometer(self, miles): 
        """Soma a quantidade especificada ao valor de leitura do hodômetro."""
        self.odometer_reading += miles
   
    def fill_gas_tank(self):
        """Carros têm tanques de gasolina."""
        return "This car need a gas tank!"

class ElectricCar(Car):
    """Representa aspectos específicos de veículoselétricos."""

    def __init__(self, make, model, year): 
        """Inicializa os atributos da classe pai Em seguida, inicializa os atributos específicos de um carro elétrico """
        super().__init__(make, model, year) 
        #   self.battery_size = 70
        self.battery = Battery()#Instâncias como atributos

    def fill_gas_tank(self):
        """Carros elétricos não têm tanques de gasolina."""
        return "This car doesn't need a gas tank!"
        


class Battery(): 
    """Uma tentativa simples de modelar uma bateria para um carro elétrico."""
    
    def __init__(self, battery_size=70): 
        
        """Inicializa os atributos da bateria."""

        self.battery_size = battery_size
        
    def describe_battery(self):
        """Exibe uma frase que descreve a capacidade da bateria."""
        return "This car has a " + str(self.battery_size) + "-kWh battery."

    def get_range(self): 
        """Exibe uma frase sobre a distância que o carro é capaz de percorrer com essa bateria."""
        if self.battery_size == 70: 
            range = 240
        elif self.battery_size == 85: 
            range = 270
        
        message = "This car can go approximately " + str(range) 
        message += " miles on a full charge."
        return message


my_tesla = ElectricCar('tesla', 'model s', 2016)

print(my_tesla.get_descriptive_name()) 
#print(my_tesla.describe_battery())
print(my_tesla.battery.describe_battery()) #Instâncias como atributos
print(my_tesla.fill_gas_tank())
print(my_tesla.battery.get_range())