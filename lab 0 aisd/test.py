import time
import tracemalloc
t_start = time.perf_counter()
tracemalloc.start()

#Вставь сюда код любой из задач чтобы проверить ее на затраты времени и памяти

print(time.perf_counter() - t_start)
print(tracemalloc.get_traced_memory()[1] / 1024 / 1024, "Mбайт")
tracemalloc.stop()
