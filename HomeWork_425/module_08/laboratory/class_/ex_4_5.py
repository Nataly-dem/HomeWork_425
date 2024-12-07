"""Не уверена, что верно поняла задание """

class Employer:

    def __init__(self, name, surname, age):
        self.__name = name
        self.__surname = surname
        self.__age = age

    def __str__(self):
        return f"{self.__name} {self.__surname}"

    def __int__(self):
        return f"Возрост служащего {self.__age}"


    def position(self):
        print("This is Employer class")


class President(Employer):

    def position(self):
        print("This is President class")


class Manager(Employer):

    def position(self):
        print("This is Manager class")

class Worker(Employer):

    def position(self):
        print("This is Worker class")


