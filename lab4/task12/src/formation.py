import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.join(current_dir, '..', '..')
sys.path.insert(0, src_dir)

from utils import read_from_file, write_in_file, measuring

def formation(n, commands):
    left = {i: 0 for i in range(1, int(n) + 1)} 
    right = {i: 0 for i in range(1, int(n) + 1)}

    head = 1
    tail = 1

    results = []

    for command in commands:
        command = command.split(" ")
        cmd = command[0]

        if cmd == "left":
            i, j = int(command[1]), int(command[2])
            left[i] = left[j]
            right[i] = j
            if left[j] != 0:
                right[left[j]] = i
            left[j] = i
            if head == j:
                head = i

        elif cmd == "right":
            i, j = int(command[1]), int(command[2])
            right[i] = right[j]
            left[i] = j
            if right[j] != 0:
                left[right[j]] = i
            right[j] = i
            if tail == j:
                tail = i

        elif cmd == "leave":
            i = int(command[1])
            if left[i] != 0:
                right[left[i]] = right[i]
            if right[i] != 0:
                left[right[i]] = left[i]
            if head == i:
                head = right[i]
            if tail == i:
                tail = left[i]
            left[i] = 0
            right[i] = 0

        elif cmd == "name":
            i = int(command[1])
            results.append(f"{left[i]} {right[i]}")
    return results

if __name__ == '__main__':
    data = read_from_file(1, 'lab4/task12/txtf/input.txt')

    n, m, commands = data[0], data[1], data[2:]
    result = formation(n, commands)
    write_in_file('lab4/task12/txtf/output.txt', result)

    measuring(1e2, formation, n, commands)