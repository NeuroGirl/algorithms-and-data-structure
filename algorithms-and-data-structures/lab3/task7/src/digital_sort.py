import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.join(current_dir, '..', '..')
sys.path.insert(0, src_dir)

from utils import read_from_file, write_in_file, measuring

def radix_sort_phase(strings, phase):
    """Сортировка по заданной фазе (символу)."""
    return sorted(strings, key=lambda x: x[1][phase-1])

if __name__ == "__main__":
    data = read_from_file('algorithms-and-data-structures/lab3/task7/txtf/input.txt')
    n, m, k, columns = int(data[0]), int(data[1]), int(data[2]), data[3:]

    # Проверка корректности входных данных
    if (1 <= n <= 10**6) and (1 <= k <= m <= 10**6) and (n * m <= 5 * 10**7):
        # Формируем список строк из колонок
        strings = [(i + 1, ''.join(columns[j][i] for j in range(m))) for i in range(n)]

        # Применяем сортировку по фазам
        for phase in range(min(m, k) - 1, -1, -1):
            strings = radix_sort_phase(strings, phase)

        # Подготовка результатов (выводим индексы строк в новом порядке)
        result = [str(item[0]) for item in strings]
        write_in_file('algorithms-and-data-structures/lab3/task7/txtf/output.txt', result)
        measuring(radix_sort_phase, strings, phase)
    else:
        print('Введите корректные данные')
    
