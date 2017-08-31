#!/usr/bin/env /usr/local/bin/python3
# -*- coding: utf-8 -*-
'''
Created on 2017年8月30日

@author: lixianjian
'''


def quick_sort(a, low, high):
    # 快速排序
    if low > high:
        return a
    mid = a[low]
    i = low + 1
    head, tail = low, high
    while head < tail:
        if a[i] > mid:
            a[tail], a[i] = a[i], a[tail]
            tail -= 1
        else:
            a[head], a[i] = a[i], a[head]
            head += 1
            i += 1

    a[head] = mid
    quick_sort(a, low, head - 1)
    quick_sort(a, head + 1, high)
    return a


def merge(left, right):
    i, j = 0, 0
    result = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result


def merge_sort(nums):
    # 归并排序
    if len(nums) <= 1:
        return nums

    num = len(nums) // 2
    left = merge_sort(nums[:num])
    right = merge_sort(nums[num:])
    nums = merge(left, right)
    return nums


# 整数排序 II
# 给一组整数，按照升序排序。使用归并排序，快速排序，堆排序或者任何其他 O(n log n) 的排序算法。
# 总耗时: 2942 ms
class Solution:

    def merge(self, A, llow, lhigh, rlow, rhigh):
        i, j = 0, 0
        low = llow
        left = A[llow:lhigh]
        right = A[rlow:rhigh]
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                A[low] = left[i]
                i += 1
            else:
                A[low] = right[j]
                j += 1
            low += 1
        if left[i:]:
            A[low:rhigh] = left[i:]
        elif right[j:]:
            A[low:rhigh] = right[j:]

    def merge_sort(self, A, llow=0, rhigh=0):
        # 归并排序
        length = rhigh - llow
        if length <= 1:
            return

        num = llow + length // 2
        self.merge_sort(A, llow, num)
        self.merge_sort(A, num, rhigh)
        self.merge(A, llow, num, num, rhigh)

    def sortIntegers2(self, A):
        # Write your code here
        # 归并排序
        self.merge_sort(A, 0, len(A))

import math


class Solution2:

    def sortIntegers2(self, A, radix=10):
        k = int(math.ceil(math.log(max(A), radix)))
        bucket = [[] for i in range(radix)]
        for i in range(1, k + 1):
            for j in A:
                bucket[j // (radix**(i - 1)) % (radix**i)].append(j)
                del A[:]
            for z in bucket:
                A += z
        del z[:]
        return A

if __name__ == '__main__':
    #     nums = [5, 2, 100, 7, 1, 6, 4, 3, 200, 1000]
    #     nums = [4, 5, 1, 2, 3]
    #     quick_sort(nums, low=0, high=len(nums) - 1)
    #     merge_sort(nums)
    #
    #     print(nums)
    s = Solution()
    A = [4, 5, 1, 2, 3]
    s.sortIntegers2(A)
    print(A)
