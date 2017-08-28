#!/usr/bin/env /usr/local/bin/python3
# -*- coding: utf-8 -*-
'''
Created on 2017年8月24日

@author: lixianjian
'''


class Solution:
    # @param A: Given an integer array
    # @return: void

    def heapify(self, A):
        # write your code here
        # print(type(A))
        length = len(A)
        average = length - 1 // 2
        for i in range(0, average + 1):
            # self.heap_sort_small(A, average - i, length)
            self.heap_sort_large(A, average - i, length)
        return A

    def heap_sort_small(self, A, i, length):
        l = 2 * i + 1
        r = 2 * i + 2
        smallest = i
        if l < length and A[l] < A[smallest]:
            smallest = l

        if r < length and A[r] < A[smallest]:
            smallest = r

        if smallest != i:
            A[i], A[smallest] = A[smallest], A[i]
            # smallest, i = i, smallest
            self.heap_sort_small(A, smallest, length)

    def heap_sort_large(self, A, i, length):
        l = 2 * i + 1
        r = 2 * i + 2
        largest = i
        if l < length and A[l] > A[largest]:
            largest = l

        if r < length and A[r] > A[largest]:
            largest = r

        if largest != i:
            A[i], A[largest] = A[largest], A[i]
            # smallest, i = i, smallest
            self.heap_sort_large(A, largest, length)


if __name__ == '__main__':

    s = Solution()
    print(s.heapify([3, 2, 1, 4, 5]))
    print(s.heapify([6, 2, 3, 4, 5]))
    print(s.heapify([45, 39, 32, 11]))
