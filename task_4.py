"""
4) Реализуйте базовый класс Car. У данного класса должны быть следующие
атрибуты: speed, color, name, is_police (булево). А также методы: go, stop,
turn(direction), которые должны сообщать, что машина поехала, остановилась,
повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar,
WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed, который должен
показывать текущую скорость автомобиля. Для классов TownCar и WorkCar
переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40
(WorkCar) должно выводиться сообщение о превышении скорости.
"""


class Car:
    """creating a car class"""

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f"{self.name} начала движение"

    def stop(self):
        return f"{self.name} остановилась"

    def turn(self, direction):
        return f"{self.name} повернула {direction}"

    def show_speed(self):
        return f"Скорость автомобиля {self.name} равна {self.speed}"


class TownCar(Car):
    """creating a TownCar class"""

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f"Скорость городского автомобиля {self.name} ровна {self.speed}")

        if self.speed > 60:
            return f"Автомобиль {self.name} нарушил скоростной режим"
        else:
            return f"Автомобиль {self.name} не нарушил скоростной режим"


class WorkCar(Car):
    """creating a WorkCar class"""

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f"Скорость рабочего автомобиля {self.name} ровна {self.speed}")

        if self.speed > 60:
            return f"Автомобиль {self.name} нарушил скоростной режим"
        else:
            return f"Автомобиль {self.name} не нарушил скоростной режим"


class SportCar(Car):
    """creating a SportCar class"""

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def sport_car(self):
        if self.is_police:
            return f"Автомобиль {self.name} является спортивным"
        else:
            return f"Автомобиль {self.name} не является спортивным"


class PoliceCar(Car):
    """creating a PoliceCar class"""

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police_car(self):
        if self.is_police:
            return f"В {self.name} менты"
        else:
            return f"В {self.name} не менты"


VAZ_2110 = TownCar(70, "Баклажан", "VAZ_2110", False)
Lada_largus = WorkCar(60, "Мокрый асфальт", "Lada_largus", False)
Lamborghini = SportCar(260, "Жёлтый", "Lamborghini", False)
Fiat = PoliceCar(90, "Белый", "Fiat", True)

print(Lada_largus.turn("в обратном направлении"))
print(f"Когда {VAZ_2110.turn('направо')} ,то {Lamborghini.stop()}")
print(f"{Lada_largus.go()} со скоростью {Lada_largus.show_speed()}")
print(f"{Lada_largus.name} цвета {Lada_largus.color}")

print(f"{Lamborghini.name} полицейская машина? {Lamborghini.is_police}")
print(f"{Lada_largus.name} полицейская машина? {Lada_largus.is_police}")

print(Lamborghini.show_speed())
print(VAZ_2110.show_speed())
print(Fiat.police_car())
print(Fiat.show_speed())
