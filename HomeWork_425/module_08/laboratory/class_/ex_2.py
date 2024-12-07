class Engine:

    def __init__(self, volume, power):
        self.__volume = volume
        self.__power = power

    def get_volume_engine(self):
        return self.__volume

    def get_power_engine(self):
        return self.__power

    def set_power_engine(self, power):
         self.__power = power

    def add_engine(self):
        engine_list = []
        engine_list.append(self.__volume)
        engine_list.append(self.__power)
        return engine_list


class Wheel:

    def __init__(self, diameter, pressure):
        self.__diameter = diameter
        self.__pressure = pressure

    def get_diameter_wheel(self):
        return self.__diameter

    def get_dpressure_wheel(self):
        return self.__pressure

    def set_pressure_wheel(self, pressure):
        self.__pressure = pressure

    def add_wheel(self):
        wheel_list = []
        wheel_list.append(self.__diameter)
        wheel_list.append(self.__pressure)
        return wheel_list

class Door:

    def __init__(self, quantity, window_regulator):
        self.__quantity = quantity
        self.__window_regulator = window_regulator

    def get_quantity_door(self):
        return self.__quantity

    def get_window_regulator_door(self):
        return self.__window_regulator

    def get_window_regulator_door(self, window_regulator):
        self.__window_regulator = window_regulator

    def add_door(self):
        door_list = []
        door_list.append(self.__quantity)
        door_list.append(self.__window_regulator)
        return door_list

class CarComp:
    def __init__(self, engine_obj: object = Engine, wheel_obj: object = Wheel, door_obj: object = Door):
        self.engine = engine_obj
        self.wheel = wheel_obj
        self.door = door_obj


