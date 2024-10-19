import time
import tracemalloc

import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.join(current_dir, '..', '..')
print(src_dir)
sys.path.insert(0, src_dir)

from task3.src.task3 import search_inversions

start_time = time.perf_counter()
tracemalloc.start()
list_to_sort = [1]
list_copy = list_to_sort.copy()

result = search_inversions(list_to_sort, list_copy, 0, len(list_to_sort)-1)
print(result)
print('Время работы: ' + str((time.perf_counter() - start_time)))
print('Память: ' + str(tracemalloc.get_traced_memory()[1]/1024**2) + ' Мб')
tracemalloc.stop()