import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.join(current_dir, '..', '..')
sys.path.insert(0, src_dir)

from utils import read_from_file, write_in_file, measuring

def bracet_counter(line):
    stack = []
    matching_brackets = {')': '(', ']': '['}

    for char in line:
        if char in "([":  # Если открывающая скобка
            stack.append(char)
        elif char in ")]":  # Если закрывающая скобка
            if stack and stack[-1] == matching_brackets[char]:
                stack.pop()
            else:
                return False  # Если не соответствует, последовательность неправильная
    return not stack

def bracet_counter_cycled(n, lines):
    results = []
    for line in lines:
        results.append("YES\n" if bracet_counter(line) else "NO\n")
    return results

if __name__ == '__main__':
    data = read_from_file(0, 'algorithms-and-data-structures/lab4/task3/txtf/input.txt')

    n, lines = data[0], data[1:]
    result = bracet_counter_cycled(n, lines)
    write_in_file('algorithms-and-data-structures/lab4/task3/txtf/output.txt', result)

    measuring(1e2, bracet_counter_cycled, n, lines)