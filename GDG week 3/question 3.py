class Cars:
    def __init__(self, make):
        self.make = make

    def get_make(self):
        return self.make
    
car = Cars("Toyota")
print(car.get_make())