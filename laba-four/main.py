"""
Ротанов Дмитрий Играрович
Лабораторная №3
Пусть дан файл data.csv, в котором содержится информация в соответствии с вариантом:
Считайте информацию из файла в соответствующую структуру (класс): +
2.1. Выведите информацию об объектах, отсортировав их по одному полю (строковому).+
2.2. Выведите информацию об объектах, отсортировав их по одному полю (числовому).+
2.3. Выведите информацию, соответствующую какому-либо критерию +
(например, для студентов - тех, у кого возраст больше какого-либо значения) +
Добавьте к программе возможность сохранения новых данных обратно в файл. +
Задание - Студенты: №, ФИО, email, группа+
"""


import pandas as pd
from studentlist import StudentList
from student import Student


def read_csv(config_path):
    """
    Считывает данные из файла CSV в DataFrame
    """
    return pd.read_csv(config_path)


def write_students_to_csv(students, filename):
    """
    Запись студентов в csv файл
    """
    data = []
    for student in students:
        data.append([student.get_number(),
                     student.get_fullname(),
                     student.get_email(),
                     student.get_group(),
                     student.get_age()])
    df = pd.DataFrame(data, columns=['№', 'ФИО', 'email', 'группа', 'возраст'])
    df.to_csv(filename, index=False)


def main():
    """
    Основная функция программы.
    """
    # Считываем данные из файла CSV в DataFrame
    config_path = '../data/data.csv'
    write_path = '../data/update_data.csv'
    data = read_csv(config_path)

    student_list = StudentList()
    for index, row in data.iterrows():
        student_list.add(row['№'], row['ФИО'], row['email'], row['возраст'], row['группа'])

    print("Исходные данные:\n", student_list)

    # 2.1. Сортировка по строковому полю (ФИО)
    student_list.sorting(key=lambda x: x.get_fullname())
    print("Отсортированные по ФИО данные:\n", student_list)

    # 2.2. Сортировка по числовому полю (возраст студента)
    student_list.sorting(key=lambda x: x.get_age())
    print("Отсортированные по возрасту данные:\n", student_list)

    # 2.3. Фильтрация данных по критерию (возраст студента больше 20 лет)
    student_list.remove_items(lambda x: x.get_age() <= 20)
    print("\nДанные, где возраст студента больше 20 лет:")
    print(student_list)

    # Добавьте к программе возможность сохранения новых данных обратно в файл.
    # Для примера сохраню отфильтрованные данные по возрасту
    write_students_to_csv(student_list, write_path)


if __name__ == '__main__':
    main()