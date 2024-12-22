import sys
import os

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.join(CURRENT_DIR, '..', '..')
sys.path.insert(0, SRC_DIR)

from utils import read_from_file, write_in_file, measuring

def phone_book(data):
    book = {}
    results = []
    i = 0
    while i < len(data):
        if data[i] == "add":
            number, name = data[i+1], data[i+2]
            book[number] = name
            i += 3
        elif data[i] == "del":
            number = data[i+1]
            book.pop(number, None)
            i += 2
        elif data[i] == "find":
            number = data[i+1]
            results.append(book.get(number, "not found")+"\n")
            i += 2
    return results

if __name__ == '__main__':
    data = read_from_file(0, 'lab6/task2/txtf/input.txt')
    n = int(data[0])
    versitiles = data[1:]
    result = phone_book(versitiles)
    write_in_file('lab6/task2/txtf/output.txt', result)

    measuring(1e2, phone_book, versitiles)