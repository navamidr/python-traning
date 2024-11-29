class Vechicle:
  def __init__(self, brand , model):
    self.brandname = brand
    self.modelname= model

  def display_info(self):
    print("brand:",self.brandname, "\nmodel:",self.modelname)

class Car(Vechicle):
    def __init__(self, brand, model,number_door):
        super().__init__(brand, model)
        self.doors=number_door

    def display(self):
      super().display_info()
      print("number of door:",self.doors)
  
class Bike(Vechicle):
    def __init__(self, brand, model,engine_capacity ):
        super().__init__(brand, model)
        self.capacity=engine_capacity 

    def display(self):
       super().display_info()
       print("engine_capacity :",self.capacity)

car=Car(brand="BMW",model="sedans",number_door=4)
bike=Bike(brand="Yamaha",model="MT 15 v2.0",engine_capacity=200)

car.display()
bike.display()
    
