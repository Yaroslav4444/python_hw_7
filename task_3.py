"""
3) Реализовать базовый класс Worker (работник), в котором определить атрибуты:
name, surname, position (должность), income (доход). Последний атрибут должен
быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность)
на базе класса Worker. В классе Position реализовать методы получения полного
имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса
Position, передать данные, проверить значения атрибутов, вызвать методы
экземпляров).
"""


class Worker:
    """creating an employee class"""

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    """creating a job class"""

    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def getting_employees_name(self):
        """method of getting the employee's name"""
        return f"{self.name} {self.surname}"

    def earning_income_bonuses(self):
        """method of earning income and bonuses"""
        return self._income["wage"] + self._income["bonus"]

    def __str__(self):
        return f"Доход сотрудника {self.name} {self.surname} " \
               f"за месяц: {self.earning_income_bonuses()} т.р."


salary_withdrawal = Position("Киркоров", "Филипп", "певец", 500000, 100000)
print(salary_withdrawal.getting_employees_name(),
      salary_withdrawal.earning_income_bonuses())
print(salary_withdrawal)
