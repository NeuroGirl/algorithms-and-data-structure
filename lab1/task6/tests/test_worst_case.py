import time
import tracemalloc

import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.join(current_dir, '..', '..')
print(src_dir)
sys.path.insert(0, src_dir)

from task6.src.task6 import bubble_sort


start_time = time.perf_counter()
tracemalloc.start()
list_to_sort = [ x * 10**6 for x in range(10 ** 3, 1, -1)]

result = bubble_sort(len(list_to_sort), list_to_sort)
print(*result)
print('Время работы: ' + str((time.perf_counter() - start_time)))
print('Память: ' + str(tracemalloc.get_traced_memory()[1]/1024**2) + ' Мб')
tracemalloc.stop()