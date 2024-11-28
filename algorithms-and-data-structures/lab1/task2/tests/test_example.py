import time
import tracemalloc

import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.join(current_dir, '..', '..')
print(src_dir)
sys.path.insert(0, src_dir)

from task2.src.task2 import insertion_sort_advanced


start_time = time.perf_counter()
tracemalloc.start()
list_to_sort = [1, 8, 4, 2, 3, 7, 5, 6, 9, 0]

result = insertion_sort_advanced(len(list_to_sort), list_to_sort)
print(*result[0])
print(*result[1])
print('Время работы: ' + str((time.perf_counter() - start_time)))
print('Память: ' + str(tracemalloc.get_traced_memory()[1]/1024**2) + ' Мб')
tracemalloc.stop()