#create an  electric car class that inherits
# from car class and has an additional attribute battery size

from Car import Car
class ElectricCar(Car):
    def __init__(self,brand,car,model,batterysize):
        super().__init__(brand,car,model)
        self.batterysize = batterysize
    
    def printself(self):
        parent = super().fucntionality()
        return f"{parent} the battery size of car is {self.batterysize}"
    def fuelType(self):
        return "Electric charge"

MyElectricCar = ElectricCar("Tesla","Hyundai",2020,"85KWH")
print(MyElectricCar.printself())
print(MyElectricCar.fuelType())


