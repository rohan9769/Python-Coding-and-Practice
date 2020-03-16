#Santro subclass implements the abstract method of superclass Car(abs.py)
from abs import Car
class Santro(Car):
    def steering(self):
        print('Santro uses race steering')
    def braking(self):
        print('Santro uses electric ABS brakes')

s=Santro('MH0455')
s.opentank()
s.steering()
s.braking()
