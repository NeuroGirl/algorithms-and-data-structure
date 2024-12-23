import random
import time
import psutil
import os


def generate_random_array_queue(n):
    array = []
    positive_turns = 0
    negative_turns = 0
    for _ in range(n):
        if positive_turns == negative_turns:
            array.append("+"+ str(random.randint(1, 10**6)))
            positive_turns += 1
        elif positive_turns > negative_turns:
            array.append(random.choice(["+"+ str(random.randint(1, 10**6)), "-"]))
            if array[-1][0] == '-':
                negative_turns += 1
            else:
                positive_turns += 1
            
    return array


def measuring(mult, task_func, *args):

    start_time = time.perf_counter()
    result = task_func(*args)
    end_time = time.perf_counter() - start_time

    memory = psutil.Process().memory_info().rss / 1024 ** 2

    print(f"Time: {end_time * mult} sec")
    print(f"Memory: {memory} Mb")


def read_from_file(num, filename, type=int):
    # Используем переменную окружения для корректного пути к файлу
    txtf_path = os.environ.get('TXT_FILE_PATH', '')
    filepath = os.path.join(filename)

    with open(filepath, "r") as f:
        if type == str:
            data = f.read()
            print(f"Input data: {data}")
            return data
        if num == 1:
            first_line = f.readline().split(" ")
            n, m = int(first_line[0]), int(first_line[1])
            data = [n, m]
            for _ in range(m):
                data.append(f.readline())
        else:
            data = list(map(str, f.read().split()))
        f.close()
        print(f"Input data: {data}")
        return data


def write_in_file(filename, data):
    # Используем переменную окружения для корректного пути к файлу
    txtf_path = os.environ.get('TXT_FILE_PATH', '')
    filepath = os.path.join(filename)

    with open(filepath, "w") as f:
        if isinstance(data, str):
            f.write(data)
        else:
            f.write("".join(map(str, data)))
        f.close()
        print(f"Output data: {data}")