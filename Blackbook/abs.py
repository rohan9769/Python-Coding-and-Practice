#This is an abstract car class
from abc import *
class Car(ABC):
    def __init__(self,regno):
        self.regno = regno

    def opentank(self):
        print(f'Fill in the fueltank of the car with registration no : {self.regno}')

    @abstractmethod
    def steering(self):
        pass
    @abstractmethod
    def braking(self):
        pass