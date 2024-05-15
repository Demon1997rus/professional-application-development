"""
Ротанов Дмитрий Играрович ВТАСбзу-21
Задание - Студенты: №, ФИО, email, группа
1) Класс должен содержать итератор
2) Должна быть реализована перегрузка стандартных операций (__str__ или __rep__, например)
3) Должно быть реализовано наследование
4) Запись значений в свойства - только через setattr
5) Возможность доступа к элементам коллекции по индексу (getitem)
6) Должны быть реализованы статические методы
7) Должны быть реализованы генераторы
"""


class Person:
    def __init__(self, number, fullname, email, age):
        """
        Конструктор класcа Person
        :param number: Номер
        :param fullname: Полное имя
        :param email: Электронная почта
        :param age: Возраст
        """
        self.__number = number
        self.__fullname = fullname
        self.__email = email
        self.__age = age

    def __setattr__(self, key, value):
        """
        Вызывается, когда атрибуту объекта выполняется присваивание
        """
        if key == '_Person__number' or key == '_Person__fullname' or key == '_Person__email' or key == '_Person__age':
            self.__dict__[key] = value
        else :
            raise AttributeError

    def __str__(self):
        """
        Преобразование объекта к строковому представлению, вызывается, когда
        объект передается функциям print(Person)) и str(Person))
        """
        return str(f'Номер - {self.__number}, '
                   f'Полное имя - {self.__fullname}, '
                   f'Электронная почта - {self.__email}, '
                   f'Возраст - {self.__age}')

    def get_number(self):
        """
        Геттер для получения номера
        """
        return self.__number

    def get_fullname(self):
        """
        Геттер для получения полного имени
        """
        return self.__fullname

    def get_email(self):
        """
        Геттер для получения электронный почты
        """
        return self.__email

    def get_age(self):
        """
        Геттер для получения возраста
        """
        return self.__age

    def set_number(self, value):
        """
        Сеттер для номера
        """
        self.__number = value

    def set_fullname(self, value):
        """
        Сеттер для полного имени
        """
        self.__fullname = value

    def set_email(self, value):
        """
        Сеттер для электронной почты
        """
        self.__email = value

    def set_age(self, value):
        """
        Сеттер для возраста
        """
        self.__age = value

    @staticmethod
    def isAdult(age):
        """
        Статический метод - возращает true если возраст выше совершеннолетнего, в противном случае false
        """
        return int(age) >= 18


if __name__ == '__main__':
    p = Person(1, 'Ротанов Дмитрий Играрович', 'rotanov.1997@email.ru', 26)


