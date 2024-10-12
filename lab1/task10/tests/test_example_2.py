import time
import tracemalloc

import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.join(current_dir, '..', '..')
print(src_dir)
sys.path.insert(0, src_dir)

from task10.src.task10 import polyndrome


start_time = time.perf_counter()
tracemalloc.start()
list_to_sort = "QAZQAZ"

result = polyndrome(len(list_to_sort), list_to_sort)
print(result)
print('Время работы: ' + str((time.perf_counter() - start_time)))
print('Память: ' + str(tracemalloc.get_traced_memory()[1]/1024**2) + ' Мб')
tracemalloc.stop()