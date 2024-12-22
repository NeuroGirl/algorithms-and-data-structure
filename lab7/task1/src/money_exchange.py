import sys
import os

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.join(CURRENT_DIR, '..', '..')
sys.path.insert(0, SRC_DIR)

from utils import read_from_file, write_in_file, measuring

def min_coins(money: int, coins: list[int]) -> float:
    list_with_count_for_coints = [float('inf')] * (money + 1)
    list_with_count_for_coints[0] = 0
    for coin in coins:
        coin = int(coin)
        for i in range(coin, money + 1):
            list_with_count_for_coints[i] = min(list_with_count_for_coints[i], list_with_count_for_coints[i - coin] + 1)

    return list_with_count_for_coints[money]


if __name__ == '__main__':
    data = read_from_file(0, 'lab7/task1/txtf/input.txt')
    summ = int(data[0])
    versitiles = data[2:]
    result = str(min_coins(summ, versitiles))
    write_in_file('lab7/task1/txtf/output.txt', result)

    measuring(1e2, min_coins, summ, versitiles)