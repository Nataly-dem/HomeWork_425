import math



class Circle:

    def __init__(self, radius):
        self.__radius = radius


    def get_diameter(self):
        return self.__radius*2

    def get_radius(self):
        return self.__radius

    def set_radius(self, radius):
        self.__radius = radius

    def circle_length(self):
        c = 2*math.pi*self.__radius
        return f'Длина окружности: {round(c, 2)}'

    def circle_area(self):
        circle_s = self.__radius**2 * math.pi
        return f"Окружность площадью: {round(circle_s, 2)}"

class Square:
    def __init__(self,side):
        self.__side = side

    def get_side(self):
        return self.__side

    def set_side(self, side):
        self.__side = side

    def square_areal(self):
        square_s = self.__side**2
        return f"Квадрат площадью: {round(square_s, 2)}"

class CircleInSquare(Circle, Square):

    def __init__(self, radius, side):
        Circle.__init__(self, radius)
        Square.__init__(self, side)

    def circle_in_square(self):
        if self.get_side() >= self.get_diameter():
            return f'{Circle.circle_area(self)} можно вписать в {Square.square_areal(self)} '
        else:
            return f'{Circle.circle_area(self)} нельзя вписать в {Square.square_areal(self)} '






