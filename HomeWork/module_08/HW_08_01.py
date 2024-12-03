"задание 8.1.1"
class Vehicle:

    def __init__(self, name, mileage ):
        self.name = name
        self.mileage = mileage


    def get_vehicle_type(self, vehicle_type):
        self.vehicle_type = vehicle_type
        if vehicle_type == 2:
            return f'Это мотоцикл марки {self.name}'
        elif vehicle_type == 3:
            return f'Это трицикл марки {self.name}'
        elif vehicle_type == 4:
            return f'Это автомабиль марки {self.name}'
        else:
            return "я не знаю таких ТС"

    def get_vehicle_advice(self):
        if self.mileage < 50000:
            return f'Неплохо, {self.name} можно брать'
        elif 50001 < self.mileage < 100000:
            return f'{self.name} надо внимательно проверить'
        elif 100001 < self.mileage < 150000:
            return f'{self.name} надо провести полную диагностику'
        else:
            return f'{self.name} лучше не брать'


car_1 =  Vehicle("kia", 5000)
car_2 =  Vehicle("BMV", 50600)
car_3 =  Vehicle("Aydi", 100005)
car_4 =  Vehicle("Lada", 570000)

print(car_1.get_vehicle_type(2))
print(car_1.get_vehicle_advice())
print()
print(car_2.get_vehicle_type(4))
print(car_2.get_vehicle_advice())
print()
print(car_3.get_vehicle_type(3))
print(car_3.get_vehicle_advice())
print()
print(car_4.get_vehicle_type(5))
print(car_4.get_vehicle_advice())
print()


"""Задание 8.1.2 """

class present:

    def __init__(self, price, recipient, package):
        self.price = price
        self.recipient = recipient
        self.package = package

    def get_presrnt_price(self):
        if self.price < 1000:
            return f'на {self.price} можно купить символический подарок {self.recipient}'
        elif 1000 < self.price < 5000:
            return f'на {self.price} можно купить хороший подарок {self.recipient}'
        else:
            return f'на {self.price} можно купить отличный подарок {self.recipient}'

    def get_present_package(self):
        if self.package == "пакет":
            return f'Подарок в упаковке {self.package} ,будет стоить {self.price + 200} руб'
        elif self.package == "коробка":
            return f'Подарок в упаковке {self.package} ,будет стоить {self.price + 500} руб'
        elif self.package == "бумага":
            return f'Подарок в упаковке {self.package} ,будет стоить {self.price + 100} руб'
        else:
            return f'Ваш подарок остается без упаковки'


present_1 = present(1050, "другу", "пакет")
present_2 = present(10000, "маме", "коробка")
present_3 = present(450, "учителю", "без упаковки")


print(present_1.get_presrnt_price())
print(present_1.get_present_package())
print()
print(present_2.get_presrnt_price())
print(present_2.get_present_package())
print()
print(present_3.get_presrnt_price())
print(present_3.get_present_package())





