from abc import ABC, abstractmethod
class Appiance(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass    

class WashingMachine(Appiance):
    def turn_on(self):
        return "Washing Machine is now ON"

    def turn_off(self):
        return "Washing Machine is now OFF"