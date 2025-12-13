class Animal:
    def make_sound(self):
        return "Animal sound"
    
class Cat(Animal):
    def make_sound(self):
        return "Meow"
    
a=Animal()
c=Cat()
print(a.make_sound())
print(c.make_sound())