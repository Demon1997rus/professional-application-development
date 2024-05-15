"""
Ротанов Дмитрий Играрович ВТАСбзу-21
Задание - Студенты: №, ФИО, email, группа
1) Класс должен содержать итератор +
2) Должна быть реализована перегрузка стандартных операций (__str__ или __rep__, например) +
3) Должно быть реализовано наследование +
4) Запись значений в свойства - только через setattr +
5) Возможность доступа к элементам коллекции по индексу (getitem) +
6) Должны быть реализованы статические методы +
7) Должны быть реализованы генераторы +
"""


from student import Student


class StudentList:
    """
    Класс, представляющий контейнер списка для объектов студентов.

    Атрибуты:
        __items (list): Приватный список для хранения объектов студентов.
        __index (int): Приватное целое число для отслеживания индекса во время итерации.

    Методы:
        __init__: Инициализирует StudentList с пустым списком.
        add: Добавляет объект студента в список.
        __getitem__: Получает объект студента из списка по индексу.
        __iter__: Инициализирует итератор для прохождения по списку.
        __next__: Возвращает следующий объект студента во время итерации.
        __str__: Возвращает строковое представление StudentList.
        __setattr__: Устанавливает значения атрибутов для определенных атрибутов.
    """

    def __init__(self):
        self.__items = []

    def add(self, item):
        """
        Метод добавления объекта студента в список.

        Args:
            item: Объект студента для добавления в список.
        """
        self.__items.append(item)

    def __getitem__(self, index):
        """
        Метод получения объекта студента из списка по индексу.

        Args:
            index: Индекс объекта студента в списке.

        Returns:
            Объект студента из списка.
        """
        return self.__items[index]

    def __iter__(self):
        """
        Метод инициализации итератора для прохождения по списку.
        """
        self.__index = 0
        return self

    def __next__(self):
        """
        Метод возвращает следующий объект студента во время итерации.
        """
        if self.__index < len(self.__items):
            item = self.__items[self.__index]
            self.__index += 1
            return item
        else:
            raise StopIteration

    def __str__(self):
        """
        Метод возвращает строковое представление StudentList.
        """
        return str(self.__items)

    def __setattr__(self, key, value):
        """
        Метод устанавливает значения атрибутов для определенных атрибутов.
        """
        if key == '_StudentList__items' or key == '_StudentList__index':
            self.__dict__[key] = value
        else:
            raise AttributeError


def student_generator(qty, names, min_age, max_age, groups):
    """
    Генератор для создания объектов студентов.

    Args:
        qty (int): Количество студентов для создания.
        names (list): Список имен студентов.
        min_age (int): Минимальный возраст студента.
        max_age (int): Максимальный возраст студента.
        groups (list): Список групп студентов.

    Yields:
        Student: Объект студента.
    """
    import random
    for i in range(qty):
        number = i + 1
        fullname = random.choice(names)
        email = fullname.lower() + "@example.com"  # Просто создаем email на основе имени
        age = random.randint(min_age, max_age)
        group = random.choice(groups)
        yield Student(number, fullname, email, age, group)


if __name__ == "__main__":
    names = ["Alice", "Bob", "Charlie", "David", "Emma"]
    groups = ["A", "B", "C", "D", "E"]
    students = student_generator(5, names, 18, 25, groups)
    for student in students:
        print(student)

