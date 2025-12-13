class  Vehicle:
    def __init__(self , brand , year):
        self.brand=brand
        self.year=year
    def info(self): 
        return(self.brand, self.year)
    
class Car(Vehicle):
    def __init__(self,brand, year, model):
        super().__init__(brand, year)
        self.model=model
    def info(self):
        return self.brand, self.year, self.model    

v= Vehicle("Toyota", 2025)
c= Car("Toyota", 2023, "Corolla")

print(v.info())
print(c.info())