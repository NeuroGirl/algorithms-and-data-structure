import time
import tracemalloc

import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.join(current_dir, '..', '..')
print(src_dir)
sys.path.insert(0, src_dir)

from task7.src.task7 import find_max

start_time = time.perf_counter()
tracemalloc.start()
list_to_find = [13, -3, -25, 20, -3, -16, -23, 18, 9, 20, -7, 12, -5, -22, 15, -4, 7]

result = find_max(list_to_find)
print(*result)
print('Время работы: ' + str((time.perf_counter() - start_time)))
print('Память: ' + str(tracemalloc.get_traced_memory()[1]/1024**2) + ' Мб')
tracemalloc.stop()