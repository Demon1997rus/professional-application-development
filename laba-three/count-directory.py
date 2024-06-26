"""
Ротанов Дмитрий Играрович
Лабораторная №3
Подсчёт количество файлов в директории и вывод на экран.
"""

import os

def count_files(directory):
    """
    Выводит в консоль количество файлов директории,
    если директории не существует, то выведет сообщение об ошибке
    """
    # Проверяем, что директория существует
    if not os.path.exists(directory):
        print("Директория не существует.")
        return

    # Получаем список файлов в директории
    files = os.listdir(directory)

    # Считаем количество файлов
    file_count = len(files)

    print(f"Количество файлов в директории '{directory}': {file_count}")

if __name__ == "__main__":
    count_files('../data')
