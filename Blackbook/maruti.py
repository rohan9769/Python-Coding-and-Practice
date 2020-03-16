#Maruti subclass implements the abstract method of superclass Car(abs.py)
from abs import Car
class Maruti(Car):
    def steering(self):
        print('Maruti uses power steering')
    def braking(self):
        print('Maruti uses ABS brakes')

m=Maruti('MH04555')
m.opentank()
m.steering()
m.braking()
