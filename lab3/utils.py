import random
import time
import psutil
import os


def generate_random_array(n, left, right):
    array = [random.randint(left, right+1) for _ in range(1, n+1)]
    return array


def measuring(task_func, *args):

    start_time = time.perf_counter()
    result = task_func(*args)
    end_time = time.perf_counter() - start_time

    memory = psutil.Process().memory_info().rss / 1024 ** 2

    print(f"Time: {end_time * 1e2} sec")
    print(f"Memory: {memory} Mb")


def read_from_file(filename: str, type=int):
    # Используем переменную окружения для корректного пути к файлу
    txtf_path = os.environ.get('TXT_FILE_PATH', '')
    filepath = os.path.join(filename)

    with open(filepath, "r") as f:
        if type == str:
            data = f.read()
            print(f"Input data: {data}")
            return data
        data = list(map(str, f.read().split()))
        print(f"Input data: {data}")
        return data


def write_in_file(filename: str, data):
    # Используем переменную окружения для корректного пути к файлу
    txtf_path = os.environ.get('TXT_FILE_PATH', '')
    filepath = os.path.join(filename)

    with open(filepath, "w") as f:
        if isinstance(data, str):
            f.write(data)
        else:
            f.write(" ".join(map(str, data)))
        print(f"Output data: {data}")