"""
5) Реализовать класс Stationery (канцелярская принадлежность). Определить в нем
 атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение
 “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil
 (карандаш), Handle (маркер). В каждом из классов реализовать переопределение
 метода draw. Для каждого из классов метод должен выводить уникальное
 сообщение. Создать экземпляры классов и проверить, что выведет описанный
 метод для каждого экземпляра.
"""


class Stationery:
    """creating a Stationery class"""

    def __init__(self, title):
        self.title = title

    @staticmethod
    def draw():
        print("Запуск отрисовки")


class Pen(Stationery):
    """creating a Pen class"""

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f"Для написания портрета использовали {self.title}")


class Pencil(Stationery):
    """creating a Pencil class"""

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f"Заметки написаны {self.title}")


class Handle(Stationery):
    """creating a Handle class"""

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f"Интересные места в книге выделены {self.title}")


Take_Pen = Pen("шариковую ручку")
Take_Pencil = Pencil("карандашом")
Take_Handle = Handle("маркером")

Take_Pen.draw()
Take_Pencil.draw()
Take_Handle.draw()
