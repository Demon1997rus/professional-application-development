"""
Ротанов Дмитрий Играрович
Лабораторная №2, 23 вариант
"""

import numpy as np
import warnings as wa

def safe_cast(val, to_type, default=None):
    """Безопасное приведение типов."""
    try:
        return to_type(val)
    except (ValueError, TypeError):
        return default

def save_to_file(matrix, sum_above_main, product_above_secondary):
    """Сохранение исходных данных и результатов в файл."""
    with open('data/matrix_results.txt', 'w') as f:
        f.write(f"Исходная матрица:\n{matrix}\n")
        f.write(f"Сумма элементов выше главной диагонали: {sum_above_main}\n")
        f.write(f"Произведение элементов выше побочной диагонали: {product_above_secondary}\n")

def generate_matrix(n):
    """Генерация квадратной матрицы размером N x N."""
    return np.random.randint(1, 10, size=(n, n))

def sum_above_main_diagonal(matrix):
    """Сумма элементов выше главной диагонали."""
    return np.sum(np.triu(matrix, k=1))

def product_above_secondary_diagonal(matrix):
    """Произведение элементов выше побочной диагонали."""
    product = 1
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            if i + j < matrix.shape[0] - 1:
                product *= matrix[i, j]
    return product

def main():
    """
    Основная функция программы.
    """
    print("Введите размер матрицы:")
    matrix_size = safe_cast(input(), int)
    if matrix_size is None:
        wa.warn("Некорректный ввод. Введите целое число!")
        return
    matrix = generate_matrix(matrix_size)
    sum_main = sum_above_main_diagonal(matrix)
    product_secondary = product_above_secondary_diagonal(matrix)
    print("Исходная матрица:\n", matrix)
    print(f"Сумма элементов выше главной диагонали: {sum_main}")
    print(f"Произведение элементов выше побочной диагонали: {product_secondary}")
    save_to_file(matrix, sum_main, product_secondary)

if __name__ == "__main__":
    main()

