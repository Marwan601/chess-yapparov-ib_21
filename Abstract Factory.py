from abc import ABC, abstractmethod
class Car(ABC):
     @abstractmethod
     def drive(self):
         pass

class CarFactory(ABC):
    @abstractmethod
    def produce_car(self):
        pass

class ElictricCar(Car):
    def drive(self):
        print('# Output: Driving an electric car.')

class PetrolCar(Car):
    def drive(self):
        print('# Output: Driving a petrol car.')

class HybridCar(Car):
    def drive(self):
        print('# Output: Driving a hybrid car.')

class ElectricCarFactory:
    def produce_car(self):
        return ElictricCar()

class PetrolCarFactory:
    def produce_car(self):
        return PetrolCar()

class HybridCarFactory:
    def produce_car(self):
        return HybridCar()

electric_factory = ElectricCarFactory()
petrol_factory = PetrolCarFactory()
hybrid_factory = HybridCarFactory()

electric_car = electric_factory.produce_car()
petrol_car = petrol_factory.produce_car()
hybrid_car = hybrid_factory.produce_car()

electric_car.drive()
# Output: Driving an electric car.
petrol_car.drive()
# Output: Driving a petrol car.
hybrid_car.drive()
# Output: Driving a hybrid car.