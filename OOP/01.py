# create a class named car with  attriutes brand and model
#  and create a instance of this class

class Car:
    def __init__(self, brand,model):
        self.brand = brand
        self.model = model
        print("This brand is "+brand+ " and the model is "+str(model))


My_Car = Car("Suzuki",2020)
MynewCar = Car("Toyota",2021)
