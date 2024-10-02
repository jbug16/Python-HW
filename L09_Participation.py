# 1
class Book:
    def __init__(self, title, publisher, pages):
        self.title = title
        self.publisher = publisher
        self.pages = pages

class Ebook(Book):
    def __init__(self, title, publisher, pages, format_):
        super().__init__(title, publisher, pages)
        self.format_ = format_

ebook = Ebook('Learn Python Programming', 'Packt Publishing', 500, 'PDF')

print(ebook.title)
print(ebook.publisher)
print(ebook.pages)
print(ebook.format_)

# 2
class Ocean:
    def __init__(self, sea_creature_name, sea_creature_size):
        self.name = sea_creature_name
        self.size = sea_creature_size

    def __str__(self):
        return f'The creature type is {self.name} and the age is {self.size}'
    
    def __repr__(self):
        return f'Ocean(\'{self.name}\', {self.size})'

c = Ocean('Jellyfish', '30 cm')
print(str(c))
print(repr(c))

# 3
# some_inheritance.py
class Engine:
    def start(self):
        return
    def stop(self):
        pass

class ElectricEngine(Engine): # Is-A Engine
    pass

class V8Engine(Engine): # Is-A Engine
    pass

class Car():
    engine_cls = Engine
    def __init__(self):
        self.engine = self.engine_cls() # Has-A Engine
    def start(self):
        print('Starting engine {0} for car {1}... Wroom, wroom!'.format(self.engine.__class__.__name__, self.__class__.__name__))
        self.engine.start()
    def stop(self):
        self.engine.stop()

class RaceCar(Car): # Is-A Car
    engine_cls = V8Engine

class CityCar(Car): # Is-A Car
    engine_cls = ElectricEngine

class F1Car(RaceCar): # Is-A RaceCar and also Is-A Car
    pass # engine_cls same as parent

car = Car()
racecar = RaceCar()
citycar = CityCar()
f1car = F1Car()

cars = [car, racecar, citycar, f1car]

for car in cars:
    car.start()

class Headlights:
    def lights_on(self):
        print('Lights are on')
        
    def lights_off(self):
        print('lights are off')