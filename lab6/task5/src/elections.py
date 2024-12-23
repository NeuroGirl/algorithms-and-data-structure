import sys
import os

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.join(CURRENT_DIR, '..', '..')
sys.path.insert(0, SRC_DIR)

from utils import read_from_file, write_in_file, measuring

def count_votes(arr):
    votes = {}

    for x in range(0, len(arr), 2):
        candidate, votes_count = arr[x], arr[x+1]
        votes_count = int(votes_count)

        if candidate in votes:
            votes[candidate] += votes_count
        else:
            votes[candidate] = votes_count
    final_votes = []
    for x in votes:
        final_votes.append(f'{x} {votes[x]}\n')
    return final_votes

if __name__ == '__main__':
    data = read_from_file(0, 'lab6/task5/txtf/input.txt')
    versitiles = data[0:]
    result = count_votes(versitiles)
    write_in_file('lab6/task5/txtf/output.txt', result)

    measuring(1e2, count_votes, versitiles)