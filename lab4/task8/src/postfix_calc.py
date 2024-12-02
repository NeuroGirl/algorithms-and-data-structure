import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.join(current_dir, '..', '..')
sys.path.insert(0, src_dir)

from utils import read_from_file, write_in_file, measuring

def postfix(expression):
    stack = []
    
    for token in expression:
        if token.isdigit():
            stack.append(int(token))
        else:
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
    
    return [stack.pop()]

if __name__ == '__main__':
    data = read_from_file(0, 'lab4/task8/txtf/input.txt')

    commands = data[1:]
    result = postfix(commands)
    write_in_file('lab4/task8/txtf/output.txt', result)

    measuring(1e2, postfix, commands)