import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.join(current_dir, '..', '..')
sys.path.insert(0, src_dir)

from utils import read_from_file, write_in_file, measuring
def queue_add_del(n, commands):
    queue = []
    deleted_from_queue = []
    for command in commands:
        if command[0] == '+':
            queue.append(command[1:]+"\n")
        if command[0] == '-':
            deleted_from_queue.append(queue.pop(0))
    return deleted_from_queue

if __name__ == '__main__':
    data = read_from_file('algorithms-and-data-structures/lab4/task2/txtf/input.txt')

    n, commands = data[0], data[1:]
    result = queue_add_del(n, commands)
    write_in_file('algorithms-and-data-structures/lab4/task2/txtf/output.txt', result)

    measuring(1e2, queue_add_del, n, commands)