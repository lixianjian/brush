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

# 摆动排序
# 给你一个没有排序的数组，请将原数组就地重新排列满足如下性质
# nums[0] <= nums[1] >= nums[2] <= nums[3]....
# 样例
# 给出数组为 nums = [3, 5, 2, 1, 6, 4] 一种输出方案为 [1, 6, 2, 5, 3, 4]
# 总耗时: 522 ms


class Solution3(object):
    """
    @param {int[]} nums a list of integer
    @return nothing, modify nums in-place instead
    """

    def wiggleSort(self, nums):
        # Write your code here
        def s(nums, low, high):
            if low > high:
                return nums
            mid = nums[low]
            i = low + 1
            head, tail = low, high
            while head < tail:
                if nums[i] > mid:
                    nums[tail], nums[i] = nums[i], nums[tail]
                    tail -= 1
                else:
                    nums[head], nums[i] = nums[i], nums[head]
                    head += 1
                    i += 1
            nums[head] = mid
            if head > self.k:
                s(nums, low, head - 1)
            else:
                s(nums, head + 1, high)
            print(nums)
            return nums

        length = len(nums)
        if length < 3:
            if length == 2:
                if nums[0] > nums[1]:
                    nums[0], nums[1] = nums[1], nums[0]
            return nums
        self.k = (length - 1) // 2
        s(nums, 0, length - 1)
        print(nums, self.k)
        self.k += 1
        if length % 2 == 0:
            for i in range(1, self.k, 2):
                nums[i], nums[self.k + i] = nums[self.k + i], nums[i]
        else:
            for i in range(1, self.k + 1, 2):
                nums[i], nums[length - i] = nums[length - i], nums[i]

        return nums

    def wiggleSortBak(self, nums):
        # Write your code here
        for i in range(1, len(nums)):
            r = i % 2
            c = nums[i - 1]
            n = nums[i]
            if (r > 0 and c > n) or (r == 0 and c < n):
                nums[i - 1], nums[i] = nums[i], nums[i - 1]


def quik_sort_review(nums, low, high):
    """ 快速排序
    """
    if low > high:
        return nums

    tmp = nums[low]
    i = low + 1
    head, tail = low, high
    while head < tail:
        if nums[tail] > tmp:
            nums[tail], nums[i] = nums[i], nums[tail]
            tail -= 1
        else:
            nums[head], nums[i] = nums[i], nums[head]
            head += 1
            i += 1
    nums[head] = tmp
    quik_sort_review(nums, low, head - 1)
    quik_sort_review(nums, head + 1, high)
    return nums


def merge_sort_review(nums):

    def merge(left, right):
        result = []
        i, j = 0, 0
        while i < len(left) and j < len(right):
            lval = left[i]
            rval = right[j]
            if lval <= rval:
                result.append(lval)
                i += 1
            else:
                result.append(rval)
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    length = len(nums)
    if length < 2:
        return nums

    mid = length // 2
    left = merge_sort_review(nums[:mid])
    right = merge_sort_review(nums[mid:])
    return merge(left, right)


def choose_sort_review(nums):
    length = len(nums)
    for i in range(length):
        for j in range(i + 1, length):
            if nums[i] <= nums[j]:
                continue
            nums[i], nums[j] = nums[j], nums[i]
    return nums


def bubble_sort_review(nums):
    length = len(nums)
    for i in range(length):
        for j in range(length - i - 1):
            if nums[j] <= nums[j + 1]:
                continue
            nums[j], nums[j + 1] = nums[j + 1], nums[j]
        print(nums)
    return nums


if __name__ == '__main__':

    # s = Solution3()
    # nums = [3, 5, 2, 1, 6, 4]
    # nums = [1, 1, 1, 1, 2]
    # s.wiggleSort(nums)
    # print(nums)

    nums = [3, 5, 2, 1, 6, 4]
    # print(quik_sort_review(nums, 0, 5))
    # print(merge_sort_review(nums))
    # print(choose_sort_review(nums))
    print(bubble_sort_review(nums))
