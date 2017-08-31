#!/usr/bin/env /usr/local/bin/python3
#-*- coding:utf-8 -*-
'''
Created on 2017年8月27日

@author: lixianjian
'''


def solution(l):
    n = l[0][0]
    r = l[0][1]
    avg = l[0][2]
    a_sum = 0
    d = {}
    for c in l[1:]:
        a = c[0]
        b = c[1]
        if b in d:
            d[b] += r - a
        else:
            d[b] = r - a
        a_sum += a
    s = n * avg - a_sum
    t_sum = 0
    keys = d.keys()
    keys.sort()
    print(d)
    print(keys)
    for key in keys:
        value = d[key]
        if s > value:
            t_sum += key * value
        elif s <= value:
            t_sum += key * s
            break
        s -= value
    return t_sum

result = solution([[5, 10, 9],
                   [0, 5],
                   [9, 1],
                   [8, 1],
                   [0, 1],
                   [9, 100], ])

print(result)
