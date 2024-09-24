class Car:
    total_Car = 0 
    
    def __init__(self, brand, car, model):
        self.__brand = brand
        self.model = model
        self.car = car
        Car.total_Car += 1  

    def get_brand(self):
        return self.__brand
    
    def functionality(self):
        return f"The brand of car is {self.__brand} {self.car}, and the model number is {self.model}"

    def fuelType(self):
        return "Petrol or Diesel"
    
    @classmethod
    def carsCount(cls):
        return f"The total number of cars is {cls.total_Car}" 


My_Car = Car("Suzuki", "Margalla", 1999)
My_NewCar = Car("Toyota", "Corolla", "2020")


print(My_Car.functionality()) 

print(My_Car.fuelType()) 
print(Car.carsCount())  