import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.join(current_dir, '..', '..')
sys.path.insert(0, src_dir)

from utils import read_from_file, write_in_file, measuring

def queue_func_min(commands):
  queue = []  
  res = []
  for command in commands:
    if command[0] == "+":
      queue.append(int(command[1:]))
    elif command[0] == "-":
      queue.pop(0)
    elif command[0] == '?':
      res.append(str(min(queue))  + "\n")
  
  return res

if __name__ == '__main__':
    data = read_from_file(0, 'lab4/task6/txtf/input.txt')

    commands = data[1:]
    result = queue_func_min(commands)
    write_in_file('lab4/task6/txtf/output.txt', result)

    measuring(1e2, queue_func_min, commands)