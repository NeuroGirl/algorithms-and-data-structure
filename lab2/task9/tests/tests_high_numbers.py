import time
import tracemalloc
import random
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.join(current_dir, '..', '..')
print(src_dir)
sys.path.insert(0, src_dir)

from task9.src.task9 import strassen_apply

start_time = time.perf_counter()
tracemalloc.start()
list_a = [random.randint(1, 10 ** 3) for _ in range(2**10)]
list_b = [random.randint(1, 10 ** 3) for _ in range(2**10)]
result = strassen_apply(2, list_a, list_b)
print(result)
print('Время работы: ' + str((time.perf_counter() - start_time)))
print('Память: ' + str(tracemalloc.get_traced_memory()[1]/1024**2) + ' Мб')
tracemalloc.stop()