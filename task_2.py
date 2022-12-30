"""
2) Реализовать класс Road (дорога), в котором определить атрибуты:
length (длина), width (ширина). Значения данных атрибутов должны передаваться
при создании экземпляра класса. Атрибуты сделать защищенными. Определить метод
расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
Использовать формулу: длинаширинамасса асфальта для покрытия одного кв метра
дороги асфальтом, толщиной в 1 см*число см толщины полотна. Проверить работу
метода.
Например: 20м*5000м*25кг*5см = 12500 т
"""

class Road:
    """creating a road class"""
    weight = 25
    thickness = 5

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calculation_asphalt_mass(self):
        """mass calculation method"""
        res = (self._length * self._width * Road.weight * Road.thickness) \
              / 1000
        print(f"Масса асфальта,необходимая для покрытия всего дорожного "
              f"полотна: {res} тонн")


asphalt_mass = Road(20, 5000)
asphalt_mass.calculation_asphalt_mass()
