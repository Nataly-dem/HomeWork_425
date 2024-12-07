"""Про попугая не стала делать, суть ясна"""

class Pets:

    def __init__(self, sound, name, pet_type):
        self.__sound = sound
        self.__name = name
        self.__pet_type = pet_type

    def get_sound(self):
        return self.__sound

    def get_name(self):
        return self.__name

    def get_type(self):
        return self.__pet_type

class Dog(Pets):

    def pet_sound(self):
        super().get_sound()
        return f"Кто это {self.get_sound()}"

    def pet_name_type(self):
        super().get_name()
        super().get_type()
        return f"Это {self.get_name()}, он {self.get_type()} и любит грызть тапочки"

class Cat(Pets):

    def pet_sound(self):
        super().get_sound()
        return f"Что-то пушистое  {self.get_sound()}"

    def pet_name_type(self):
        super().get_name()
        super().get_type()
        return f"Это {self.get_name()}, он {self.get_type()} и люит молоко"

class Hamster(Pets):

    def pet_sound(self):
        super().get_sound()
        return f"Что-то {self.get_sound()} в коробке"

    def pet_name_type(self):
        super().get_name()
        super().get_type()
        return f"Это {self.get_name()}, он {self.get_type()} и люит шуршать"

