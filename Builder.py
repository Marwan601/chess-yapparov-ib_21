from abc import ABC, abstractmethod

class Engine:
    def __init__(self, type_, volume):
        self.type = type_
        self.volume = volume

    def __str__(self):
        return f"{self.type}, {self.volume}L"

class Transmission:
    def __init__(self, type_, gears):
        self.type = type_
        self.gears = gears

    def __str__(self):
        return f"{self.type}, {self.gears} gears"

class Body:
    def __init__(self, type_, color, doors):
        self.type = type_
        self.color = color
        self.doors = doors

    def __str__(self):
        return f"{self.color} {self.type}, {self.doors} doors"

class Car:
    def __init__(self):
        self.brand = None
        self.model = None
        self.engine = None
        self.transmission = None
        self.body = None

    def __str__(self):
        return (f"Автомобиль: {self.brand} {self.model}\n"
                f"Двигатель: {self.engine}\n"
                f"Коробка передач: {self.transmission}\n"
                f"Кузов: {self.body}")

class CarBuilder(ABC):
    @abstractmethod
    def set_brand(self, brand):
        pass

    @abstractmethod
    def set_model(self, model):
        pass

    @abstractmethod
    def set_engine(self, engine_type, volume):
        pass

    @abstractmethod
    def set_transmission(self, transmission_type, gears):
        pass

    @abstractmethod
    def set_body(self, body_type, color, doors):
        pass

    @abstractmethod
    def get_car(self):
        pass

class SedanBuilder(CarBuilder):
    def __init__(self):
        self.car = Car()

    def set_brand(self, brand="Toyota"):
        self.car.brand = brand

    def set_model(self, model="Camry"):
        self.car.model = model

    def set_engine(self, engine_type="Gasoline", volume=2.5):
        self.car.engine = Engine(engine_type, volume)

    def set_transmission(self, transmission_type="Automatic", gears=6):
        self.car.transmission = Transmission(transmission_type, gears)

    def set_body(self, body_type="Sedan", color="White", doors=4):
        self.car.body = Body(body_type, color, doors)

    def get_car(self):
        return self.car

class SUVBuilder(CarBuilder):
    def __init__(self):
        self.car = Car()

    def set_brand(self, brand="Ford"):
        self.car.brand = brand

    def set_model(self, model="Explorer"):
        self.car.model = model

    def set_engine(self, engine_type="Diesel", volume=3.0):
        self.car.engine = Engine(engine_type, volume)

    def set_transmission(self, transmission_type="Automatic", gears=8):
        self.car.transmission = Transmission(transmission_type, gears)

    def set_body(self, body_type="SUV", color="Black", doors=5):
        self.car.body = Body(body_type, color, doors)

    def get_car(self):
        return self.car

class CarDirector:
    def __init__(self, builder):
        self.builder = builder

    def construct_car(self):
        self.builder.set_brand()
        self.builder.set_model()
        self.builder.set_engine()
        self.builder.set_transmission()
        self.builder.set_body()
        return self.builder.get_car()


sedan_builder = SedanBuilder()
director = CarDirector(sedan_builder)
sedan = director.construct_car()
print("Создан седан:")
print(sedan)

