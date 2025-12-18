from abc import ABC, abstractmethod
class Transport(ABC):
    @abstractmethod
    def move(self):
        pass

class bus(Transport):
    def move(self):
        print("Bus moves on road")

class Train(Transport):
    def move(self):
        print("Train moves on rails")

