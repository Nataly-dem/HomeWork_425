
class PowerUnit:

    def __init__(self, power):
        self.power = power

    def get_power(self):
        return self.power

    def apply_voltage(self):
      return f"Напряжение подано. \nБлок питание мощностью {self.power} ВТ"


class Motherboard:
    def __init__(self, chipset):
        self.chipset = chipset

    def get_chipset(self):
        return self.chipset

    def voltage_redistribution(self):
        return f'Перераспределение напряжения. \nЧипсет {self.chipset}'


class CPU:

    def __init__(self, freq,core):
        self.freq = freq
        self.core = core

    def get_freq(self):
        return self.freq

    def get_core(self):
        return self.core

    def add_cpu(self):
        cpu_list = []
        cpu_list.append(self.freq)
        cpu_list.append(self.core)
        return cpu_list

    def turbo(self):
        return f'Запущен турбо режим. \nБазовая частота процессора {self.freq} ГГЦ, количество ядер {self.core}  '


class RAM:

    def __init__(self, volume_ram, frequency):
        self.volume_ram = volume_ram
        self.frequency = frequency

    def get_volume_ram(self):
        return self.volume_ram

    def get_requency(self):
        return self.requency

    def add_ram(self):
        ram_list = []
        ram_list.append(self.volume_ram)
        ram_list.append(self.frequency)
        return ram_list

    def download(self):
        return f'Данные загружены'

    def upload_data(self):
        return f'Данные выгруженн'


class SSD:

    def __init__(self, volume_ssd):
        self.volume_ssd = volume_ssd

    def get_volume_ssd(self):
        return self.volume_ssd

    def save_data(self):
        return f'Данные сохранены'

    def remove_data(self):
        return f'Данные удалены'

class VideoCard:

    def __init__(self, model, volume):
        self.model = model
        self.volume = volume

    def get_model(self):
        return self.model

    def get_volume(self):
        return self.volume

    def get_volume_ssd(self):
        videoCard_list = []
        videoCard_list.append(self.model)
        videoCard_list.append(self.volume)
        return videoCard_list

    def display_image(self):
        return f'Изображение выведено на экран\nМодель видео карты {self.model}, обьем памяти {self.volume}Гб'


class Computer(PowerUnit, Motherboard, CPU, RAM, SSD, VideoCard):

    def __init__(self, power, chipset, freq, core, volume_ram, frequency, volume_ssd, model, volume):
        PowerUnit.__init__(self, power)
        Motherboard.__init__(self, chipset)
        CPU.__init__(self, freq,core)
        RAM.__init__(self, volume_ram, frequency)
        SSD.__init__(self, volume_ssd)
        VideoCard.__init__(self, model, volume)

    def volume_frequency(self):
        return f"Объем оперативной памяти: {self.volume_ram}ГБ\nЧастота оперативной памяти {self.frequency}Мгц"

    def volume_ssd_(self):
        return f'Объем SSD накопителя {self.volume_ssd}Mb'



computer = Computer(500, "H610", 2.5, 6, 16, 3200, 256,  "NVIDIA GeForce 1050Ti", 4 )

print(computer.apply_voltage())
print(computer.voltage_redistribution())
print(computer.turbo())
print(computer.volume_frequency())
print(computer.volume_ssd_())
print(computer.display_image())
print()
print()
"""Для композиции не стала расписывать красивую информацию, потому что так и не поняла какой вывод нужен, но все работает
Так же знаю говорили, что принты в отдельный файл надо, но задание одно решила оставить так.
 И да в компьютерах совсем ничего не понимаю....сложно """

class ComputerComp:

    def __init__(self, powerunit_obj: object = PowerUnit, motherboard_obj: object = Motherboard, cpu_obj: object = CPU, ram_obj: object = RAM,ssd_obj: object = SSD, videocard_obj: object = VideoCard):
        self.powerunit = powerunit_obj
        self.motherboard = motherboard_obj
        self.cpu = cpu_obj
        self.ram = ram_obj
        self.ssd =ssd_obj
        self.videjcard = videocard_obj


powerunit = PowerUnit(500)
motherboard = Motherboard("H610")
cpu = CPU(2.5, 6)
ram = RAM(16, 3200)
ssd = SSD(256)
videjcard = VideoCard("NVIDIA GeForce 1050Ti", 4)

computer = ComputerComp(powerunit, motherboard, cpu, ram, ssd, videjcard)

print(computer.powerunit.get_power())
print(computer.motherboard.get_chipset())
print(computer.cpu.add_cpu())
print(computer.ram.add_ram())
print(computer.ssd.get_volume_ssd())
print(computer.videjcard.get_volume_ssd())














