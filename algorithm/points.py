#!/usr/bin/env /usr/local/bin/python3
# -*- coding: utf-8 -*-
'''
Created on 2017年8月24日

@author: lixianjian
'''

import math


# Definition for a point.


class Point:

    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b


class Solution:
    # @param {Pint[]} points a list of points
    # @param {Point} origin a point
    # @param {int} k an integer
    # @return {Pint[]} the k closest points

    def kClosest(self, points, origin, k):
        # Write your code here
        distances = {}
        for point in points:
            distance = math.pow(point.x - origin.x, 2) + \
                math.pow(point.y - origin.y, 2)
            if distance in distances:
                distances[distance].append(point)
            else:
                distances[distance] = [point]

        keys = sorted(distances.keys())

        length = 0
        result = []
        for key in keys:
            value = distances[key]
            length2 = len(value)
            if length2 > 1:
                # 排序
                value = self.points_sort(value)
            if length + length2 > k:
                result.extend(value[:k - length])
                break

            result.extend(value)
            length += length2

        return result

    def points_sort(self, points):
        length = len(points)
        for i in range(length):
            p_min = points[i]
            p_cur = points[i]
            for j in range(i + 1, length):
                p_cur = points[j]
                if p_min.x > p_cur.x or \
                        (p_min.x == p_cur.x and p_min.y > p_cur.y):
                    # print((p_min.x, p_min.y), (p_cur.x, p_cur.y))
                    p_min, points[j] = p_cur, p_min
                    # print('-', (p_min.x, p_min.y), (p_cur.x, p_cur.y))
            points[i] = p_min
        return points

if __name__ == '__main__':
    s = Solution()
    # points = [[4, 6], [4, 7], [4, 4], [2, 5], [1, 1]]
    # origin = Point(0, 0)
    # k = 3

    # points = [[-1, -1], [1, 1], [100, 100]]
    # origin = Point(0, 0)
    # k = 2

    points = [[-435, -347], [-435, -347], [609, 613], [-348, -267],
              [-174, -107], [87, 133], [-87, -27], [-609, -507], [435, 453],
              [-870, -747], [-783, -667], [0, 53], [-174, -107], [783, 773],
              [-261, -187], [-609, -507], [-261, -187], [-87, -27], [87, 133],
              [783, 773], [-783, -667], [-609, -507], [-435, -347], [783, 773],
              [-870, -747], [87, 133], [87, 133], [870, 853], [696, 693],
              [0, 53], [174, 213], [-783, -667], [-609, -507], [261, 293],
              [435, 453], [261, 293], [435, 453]]
    origin = Point(-11, 199)
    k = 13

    point_objs = [Point(a, b) for a, b in points]
    print([(p.x, p.y) for p in s.kClosest(point_objs, origin, k)])
    # for p in s.points_sort(points):
    #     print((p.x, p.y))

    for x, y in [(98, -66), (11, -146), (185, 14)]:
        print(math.pow(x, 2) + math.pow(y, 2))
