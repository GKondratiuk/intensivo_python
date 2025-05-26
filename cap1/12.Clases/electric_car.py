class Car: #creamos al clase auto
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def descriptive_name(self):
        long_name = f'{self.year} {self.make} {self.model}'
        return long_name.title()
    
    def read_odometer(self):
        print(f'This car has {self.odometer_reading} miles on it')
        
    def update_odometer(self,mileage):
        
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print('you cant roll back an odometer !')
    
    def increment_odometer(self,miles):
        self.odometer_reading += miles
    

class ElectricCar(Car): #clase padre Car
    
    def __init__(self,make,model,year):
        super().__init__(make,model,year) #esto es la herencia, se obtiene de la clase padre
        self.battery_size = 40 #esto es lo nuevo, caracteristico de esta clase hija

    def descriptive_battery(self):
        print(f"this car has a {self.battery_size} kWh battery")

my_leaf = ElectricCar('nissan','leaf',2024)
print(my_leaf.descriptive_name())
my_leaf.descriptive_battery()
    