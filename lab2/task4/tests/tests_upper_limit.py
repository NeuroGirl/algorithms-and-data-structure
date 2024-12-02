import time
import tracemalloc
import random
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.join(current_dir, '..', '..')
print(src_dir)
sys.path.insert(0, src_dir)

from task4.src.task4 import start_search

start_time = time.perf_counter()
tracemalloc.start()
list_where_find = sorted([random.randint(1,  10 ** 9 + 1) for _ in range(10 ** 5)])
list_to_find = [random.choice(list_where_find) for _ in range(10 ** 4 + 50000)]
for i in range(40000):
    list_to_find.insert(random.randint(1,  10 ** 4 + 50000 +i), 0)

result = start_search(list_where_find, list_to_find)
print(*result)
print('Время работы: ' + str((time.perf_counter() - start_time)))
print('Память: ' + str(tracemalloc.get_traced_memory()[1]/1024**2) + ' Мб')
tracemalloc.stop()