#!/usr/bin/python3
'''Given a pile of coins of different values,
    determine the fewest number of coins needed to meet
    a given amount total.
'''
import sys


def makeChange(coins, total):
    '''
    Return: fewest number of coins needed to meet total
    If total is 0 or less, return 0
    If total cannot be met by any number of coins you have, return -1
    '''
    if total <= 0:
        return 0
    table = [sys.maxsize for i in range(total + 1)]
    table[0] = 0
    m = len(coins)
    for i in range(1, total + 1):
        for j in range(m):
            if coins[j] <= i:
                subres = table[i - coins[j]]
                if subres != sys.maxsize and subres + 1 < table[i]:
                    table[i] = subres + 1

    if table[total] == sys.maxsize:
        return -1
    return table[total]

if __name__ == "__main__":
    result1 = makeChange([1, 2, 25], 37)
    result2 = makeChange([1256, 54, 48, 16, 102], 1453)

    print("Result for [1, 2, 25] and total 37:", result1)
    print("Result for [1256, 54, 48, 16, 102] and total 1453:", result2)
