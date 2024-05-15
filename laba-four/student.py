"""
Ротанов Дмитрий Играрович ВТАСбзу-21
Задание - Студенты: №, ФИО, email, группа
1) Класс должен содержать итератор
2) Должна быть реализована перегрузка стандартных операций (__str__ или __rep__, например) +
3) Должно быть реализовано наследование +
4) Запись значений в свойства - только через setattr +
5) Возможность доступа к элементам коллекции по индексу (getitem)
6) Должны быть реализованы статические методы +
7) Должны быть реализованы генераторы
"""

from person import Person


class Student(Person):
    def __init__(self, number, fullname, email, age, group):
        """
        Конструктор класса Student
        :param number: Номер
        :param fullname: Полное имя
        :param email: Электронная почта
        :param age: Возраст
        :param group: Группа
        """
        Person.__init__(self, number, fullname, email, age)
        self.__group = group

    def __setattr__(self, key, value):
        if (key == '_Person__number' or
                key == '_Person__fullname' or
                key == '_Person__email' or
                key == '_Person__age' or
                key == '_Student__group'):
            self.__dict__[key] = value
        else:
            raise AttributeError
        
    def __str__(self):
        return super().__str__() + f', Группа - {self.__group}'

    def get_group(self):
        return self.__group

    def set_group(self, value):
        self.__group = value


if __name__ == '__main__':
    s = Student(1, "Ротанов Дмитрий Играрович", 'rotanov.1997@mail.ru', 26, 'ВТАСбзу-21')
    print(s.get_group())
