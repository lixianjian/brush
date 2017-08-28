#!/usr/bin/env /usr/local/bin/python3
# -*- coding: utf-8 -*-
'''
Created on 2017年8月24日

@author: lixianjian
'''


class Solution:
    # @param matrix: a matrix of integers
    # @param k: an integer
    # @return: the kth smallest number in the matrix

    def kthSmallest(self, matrix, k):
        # write your code here
        if not matrix:
            return 0
        self.matrix = matrix
        self.k = k
        self.length = 1
        self.pv = [1, 0]
        self.ph = [0, 0]
        self.values = []
        # 行数
        self.length_h = len(matrix)
        # 列数
        self.length_v = len(matrix[0])
        origin = matrix[0][0]
        self.h_max = origin
        self.v_max = origin
        self.m = origin
        # self.values.append(origin)
        if self.m > self.v_max:
            self.V()
        else:
            self.H()
        # print(self.ph, self.pv)
        print(self.values)
        return self.m

    def H(self):
        # print('--h', self.ph)
        for i in range(self.ph[0], self.length_h):
            for j in range(self.ph[1], self.length_v):
                v = self.matrix[i][j]
                if v < self.h_max:
                    continue
                if v > self.v_max and self.length_v > 1:
                    self.h_max = v
                    self.ph[0] = i
                    self.ph[1] = j
                    return self.V()

                self.values.append(v)
                self.m = v
                if self.length == self.k:
                    # print('-h', i, j)
                    return
                self.length += 1
            j = self.pv[0] + 1
            if self.length_v <= j:
                self.ph[1] = self.length_v - 1
            else:
                self.ph[1] = j

    def V(self):
        # print('--v', self.pv)
        for j in range(self.pv[1], self.length_v):
            for i in range(self.pv[0], self.length_h):
                v = self.matrix[i][j]
                if v < self.v_max:
                    continue
                if v > self.h_max and self.length_h > 1:
                    self.v_max = v
                    self.pv[0] = i
                    self.pv[1] = j
                    return self.H()

                self.values.append(v)
                self.m = v
                if self.length == self.k:
                    # print('-v', i, j)
                    return
                self.length += 1
            i = self.ph[0] + 1
            if self.length_h <= i:
                self.pv[0] = self.length_h - 1
            else:
                self.pv[0] = i


class Solution2:
    # @param matrix: a matrix of integers
    # @param k: an integer
    # @return: the kth smallest number in the matrix

    def kthSmallest(self, matrix, k):
        # write your code here
        if not matrix:
            return 0
        d = {}
        for m in matrix:
            for e in m:
                if e in d:
                    d[e] += 1
                else:
                    d[e] = 1
        keys = sorted(d.keys())
        for key in keys:
            k -= d[key]
            if k <= 0:
                return key


import heapq
 
 
class Solution3:
    # @param matrix: a matrix of integers
    # @param k: an integer
    # @return: the kth smallest number in the matrix
 
    def kthSmallest(self, matrix, k):
        h = []
        for m in matrix:
            for e in m:
                heapq.heappushpop(h, e)
        result = None
        for _ in range(k):
            result = heapq.heappop(h)
        return result


# O(klog(n))
# 总耗时: 996 ms
# import heapq
# class Solution4(object):
#     def kthSmallest(self, matrix, k):
#         v_length = len(matrix[0])
#         heap = [(row[0], i, 0) for i, row in enumerate(matrix)]
#         heapq.heapify(heap)
#         print(heap)
#         ret = 0
#         for _ in range(k):
#             ret, i, j = heapq.heappop(heap)
#             if j+1 < v_length:
#                 heapq.heappush(heap, (matrix[i][j+1], i, j+1))
#         return ret

# O(klog(n))
# 总耗时: 996 ms
import heapq
class Solution5(object):
    def kthSmallest(self, matrix, k):
        h_length = len(matrix)
        heap = [(e, 0, j) for j, e in enumerate(matrix[0])]
        heapq.heapify(heap)
        print(heap)
        ret = 0
        for _ in range(k):
            ret, i, j = heapq.heappop(heap)
            if i+1 < h_length:
                heapq.heappush(heap, (matrix[i+1][j], i+1, j))
        return ret


# # O(klog(k))
import heapq
class Solution6(object):
    def kthSmallest(self, matrix, k):
        m = len(matrix)
        n = len(matrix[0])
        heap, res = [(matrix[0][0], 0, 0)], 0
        print(heap)
        for k in range(1, k + 1):
            res, row, col = heapq.heappop(heap)
            if not row and col < n - 1:
                print(row, col + 1)
                heapq.heappush(heap, (matrix[row][col + 1], row, col + 1))
            if row < m - 1:
                print(row + 1, col)
                heapq.heappush(heap, (matrix[row + 1][col], row + 1, col))
            print(heap)
        return res


if __name__ == '__main__':

    s = Solution5()
    matrix = [
        [1, 5, 7],
        [3, 7, 8],
        [4, 8, 9],
    ]
    k = 4

#     matrix = [
#         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
#             1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
#         [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
#          2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
#         [3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
#          4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
#         [3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
#          4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7],
#         [8, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9,
#          9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
#         [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]]
#     k = 77

#     matrix = [[1], [2], [3], [100], [101], [1000], [9999]]
#     k = 5

#     matrix = [[998, 1002],
#               [998, 1003],
#               [999, 1003],
#               [1000, 1003],
#               [1000, 1004]]
#     k = 7

#     matrix = [[1, 2, 3, 4, 5],
#               [2, 3, 4, 5, 6],
#               [3, 4, 5, 6, 7],
#               [4, 5, 6, 7, 8]]
#     k = 19
    print(s.kthSmallest(matrix, k))
