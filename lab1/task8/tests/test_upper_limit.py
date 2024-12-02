import time
import tracemalloc
import random

import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.join(current_dir, '..', '..')
print(src_dir)
sys.path.insert(0, src_dir)

from task8.src.task8 import swap_sort


start_time = time.perf_counter()
tracemalloc.start()
list_to_sort = [random.randint(-10 ** 9, 10 ** 9 + 1) for _ in range(5000)]

result = swap_sort(5000, list_to_sort)

print('Время работы: ' + str((time.perf_counter() - start_time)))
print('Память: ' + str(tracemalloc.get_traced_memory()[1]/1024**2) + ' Мб')
tracemalloc.stop()
print(result)