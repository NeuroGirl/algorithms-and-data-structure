import time
import tracemalloc

import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.join(current_dir, '..', '..')
print(src_dir)
sys.path.insert(0, src_dir)

from task9.src.task9 import strassen_apply

start_time = time.perf_counter()
tracemalloc.start()
list_a = '1 2 3 4'
list_b = '9 8 7 6'
result = strassen_apply(2, list(map(int, list(list_a.split(' ')))), list(map(int, list(list_b.split(' ')))))
print(result)
print('Время работы: ' + str((time.perf_counter() - start_time)))
print('Память: ' + str(tracemalloc.get_traced_memory()[1]/1024**2) + ' Мб')
tracemalloc.stop()