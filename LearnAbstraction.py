from abc import ABC, abstractmethod
from pickle import DUP   
class Car(ABC):   
    def mileage(self):   
        pass  
  
class Tesla(Car):   
    def mileage(self):   
        print("The mileage is 30kmph")   
class Suzuki(Car):   
    def mileage(self):   
        print("The mileage is 25kmph ")   
class Duster(Car):   
     def mileage(self):   
          print("The mileage is 24kmph ")   
class Renault(Car):   
    def mileage(self):   
            print("The mileage is 27kmph ")


tesla=Tesla() 
tesla.mileage()

suzuki=Suzuki()
suzuki.mileage()

duster=Duster()
duster.mileage()

renault=Renault()
renault.mileage()

              