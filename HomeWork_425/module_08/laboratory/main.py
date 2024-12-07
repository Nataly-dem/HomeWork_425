from module_08.laboratory.class_.ex_1 import Circle, Square, CircleInSquare
from module_08.laboratory.class_.ex_2 import Engine, Wheel, Door, CarComp
from module_08.laboratory.class_.ex_3 import Dog, Cat, Hamster
from module_08.laboratory.class_.ex_4_5 import President, Manager, Worker

"""Задание 1"""
circle = Circle(10)
print(circle.circle_area())
print(circle.circle_length())


square = Square(10)
print(square.square_areal())

a= CircleInSquare(10, 20)
print(a.circle_in_square())
print()
print()

"""Задание 2"""

engine = Engine("2 литра", "192 л.с.")
wheel = Wheel(18, 2.2)
door = Door(4, "Электрический")
car = CarComp(engine, wheel ,door)

print(car.engine.add_engine())
print(car.wheel.add_wheel())
print(car.door.add_door())
print()
print()

"""задание 3"""

dog = Dog("лаит", "Шарик", "собака")
cat = Cat("мяучит","Васек","кот")
hamster = Hamster("шуршит","Пикли","хомяк")
print(dog.pet_sound())
print(dog.pet_name_type())
print()
print(cat.pet_sound())
print(cat.pet_name_type())
print()
print(hamster.pet_sound())
print(hamster.pet_name_type())
print()
print()
"""Задание 4-5"""

person_1 = President("Игорь","Балабанов","55")
person_1.position()
print(person_1.__str__())
print(person_1.__int__())
print()
person_2 = Manager("Ирина","Спижарская","33")
person_2.position()
print(person_2.__str__())
print(person_2.__int__())
print()
person_3 = Worker("Макси","Белов","25")
person_3.position()
print(person_3.__str__())
print(person_3.__int__())