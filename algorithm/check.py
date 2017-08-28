#!/usr/bin/env /usr/local/bin/python3
# -*- codeing: utf-8 -*-
'''
Created on 2017年8月22日

@author: lixianjian
'''

import math


def sum_for(l=[]):
    count = 0
    for e in l:
        count += e
    return count


def sum_while(l=[]):
    count = 0
    i = 0
    length = len(l)
    while i < length:
        count += l[i]

    return count


def sum_iter(l=[], i=0, count=0):
    if not l:
        return count

    if i >= len(l):
        return count

    return sum_iter(l, i + 1, count + l[i])


def list_turn(l1=[], l2=[]):

    if not l2:
        return l1

    if not l1:
        return l2

    l3 = []
    length1 = len(l1)
    length2 = len(l2)
    length = min(length1, length2)
    for i in range(length):
        l3.append(l1[i])
        l3.append(l2[i])

    if length1 > length:
        l3.extend(l1[length:])
    else:
        l3.extend(l2[length:])
    return l3


def fib(count=0):
    l = [0, 1]
    if count < 0:
        return []

    if count < 3:
        return l[:count]

    pre1 = 0
    pre2 = 1
    for _ in range(count - 2):
        fib_num = pre1 + pre2
        l.append(fib_num)
        pre1, pre2 = pre2, fib_num
    return l


def get_max(l=[]):
    if not l:
        return 0

    l = ['%s' % e for e in l]
    l.sort(reverse=True)
    return ''.join(l)


TARGET_SUM = 100
VALUES = [1, 2, 3, 4, 5, 6, 7, 8, 9]
VALUES_LEN = len(VALUES)


def add(digit, sign='', branches=[]):
    for i in range(len(branches)):
        branches[i] = '%d%s%s' % (digit, sign, branches[i])
    return branches


def f(_sum=0, number=0, index=1):
    results = []
    digit = abs(number) % 10
    if index == VALUES_LEN:
        if (_sum == number):
            results = [digit]
        return results

    # 1 + f(99, [2,...,9])
    branch1 = f(_sum - number, VALUES[index], index + 1)
    # 1 - f(99, [2,...,9])
    branch2 = f(_sum - number, -VALUES[index], index + 1)

    # 12 + f(88, [3,...,9])
    if number >= 0:
        concatenatedNumber = 10 * number + VALUES[index]
    else:
        concatenatedNumber = 10 * number - VALUES[index]
    branch3 = f(_sum, concatenatedNumber, index + 1)

    results.extend(add(digit, "+", branch1))
    results.extend(add(digit, "-", branch2))
    results.extend(add(digit, "", branch3))

    return results


if __name__ == '__main__':

    # print(sum_iter([1, 3, 3, 5]))
    # print(list_turn([], []))
    # print(fib(1))
    # print(get_max([50, 2, 1, 9]))
    for r in f(_sum=TARGET_SUM, number=VALUES[0], index=1):
        print(r)
