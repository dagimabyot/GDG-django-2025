class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width*self.height
    
rect = Rectangle(3, 10)
print(rect.area())