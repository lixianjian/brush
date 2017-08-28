#!/usr/bin/env /usr/local/bin/python3
# -*- coding: utf-8 -*-
'''
Created on 2017年8月22日

@author: lixianjian
'''


TARGET_SUM = 100
VALUES = [1, 2, 3, 4, 5, 6, 7, 8, 9]
VALUES_LEN = len(VALUES)


def add(digit=0, sign='', branches=[]):
    # for branch in branches:
    #     branch = '%d%s%s' % (digit, sign, branch)

    return ['%d%s%s' % (digit, sign, branch) for branch in branches]


def f(sum_=0, number=0, index=0):
    results = []
    # 获取当前使用的数字
    digit = abs(number) % 10
    if index == VALUES_LEN:
        if sum_ == number:
            # 最后取的数字（number）和需要的值(sum_)相等，则是我们需要的结果
            results = [digit]
        return results

    # sum_ = number + f([VALUES[index:])
    branch1 = f(sum_ - number, VALUES[index], index + 1)
    # sum_ = number - f([VALUES[index:])
    branch2 = f(sum_ - number, -VALUES[index], index + 1)
    # sum_ = number * 10 + VALUES[index] + f([VALUES[index+1:])
    if number < 0:
        tmp_number = number * 10 - VALUES[index]
    else:
        tmp_number = number * 10 + VALUES[index]
    branch3 = f(sum_, tmp_number, index + 1)

    results.extend(add(digit, '+', branch1))
    results.extend(add(digit, '-', branch2))
    results.extend(add(digit, '', branch3))

    return results


if __name__ == '__main__':

    for r in f(TARGET_SUM, VALUES[0], 1):
        print(r)
