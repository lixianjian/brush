#!/usr/bin/env /usr/local/bin/python3
# -*- coding: utf-8 -*-
'''
Created on 2017年8月29日

@author: lixianjian
'''

import heapq


class TestClass(object):
    """ test class in visual studio code
    """

    def __init__(self):
        """
        """
        pass

    def method1(self):
        """ method 1
        """
        pass

    def method2(self):
        """ method 2
        """
        pass


class Solution:
    """
    @param: nums: A list of integers
    @return: the median of numbers
    """

    def medianII(self, nums):
        # write your code here
        result = []
        if not nums:
            return
        result.append(nums[0])
        heap = [nums[0]]
        # heapq.heapify(heap)
        length = 1
        for n in nums[1:]:
            # heapq.heappush(heap, n)
            heap = heapq.merge(heap, [n])
            print(heap)
            result.append(heap[length // 2])
            length += 1
        return result


import bisect


class Solution2:
    """
    @param: nums: A list of integers
    @return: the median of numbers
    """

    def medianII(self, nums):
        # write your code here
        result = []
        if not nums:
            return
        result.append(nums[0])
        heap = [nums[0]]
        # heapq.heapify(heap)
        length = 1
        for n in nums[1:]:
            # heapq.heappush(heap, n)
            bisect.insort(heap, n)
            # print(heap)
            result.append(heap[length // 2])
            length += 1
        return result

# 中位数
# 给定一个未排序的整数数组，找到其中位数。
# 中位数是排序后数组的中间值，如果数组的个数是偶数个，则返回排序后数组的第N/2个数。
# 总耗时: 977 ms
# O(n)


class Solution3:
    """
    @param: nums: A list of integers
    @return: An integer denotes the middle number of the array
    """

    def median(self, nums):
        # write your code here.
        def s(a, low, high):
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
            if head == self.k:
                return a

            if head > self.k:
                s(a, low, head - 1)
            else:
                s(a, head + 1, high)
            print(a)
            return a

        length = len(nums)
        if length < 1:
            return None
        self.k = (length - 1) // 2
        s(nums, 0, length - 1)
        print(nums)
        return nums[self.k]


# 在数组中找到第k大的元素
# O(n)
# 总耗时: 321 ms
class Solution4:
    # @param k & A a integer and an array
    # @return ans a integer

    def kthLargestElement(self, k, A):
        # write your code here.
        def s(a, low, high):
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
            if head == self.k:
                return a

            if head > self.k:
                s(a, low, head - 1)
            else:
                s(a, head + 1, high)
            print(a)
            return a

        length = len(A)
        if length < 1:
            return None
        self.k = length - k
        s(A, 0, length - 1)
        print(A)
        return A[self.k]

# 两个有序列表取中文数
# 两个排序的数组A和B分别含有m和n个数，找到两个排序数组的中位数，要求时间复杂度应为O(log (m+n))。
# O(log(min(m,n))
# https://discuss.leetcode.com/topic/22406/python-o-log-min-m-n-solution#
# 总耗时: 555 ms


class Solution5:
    # @return a float

    def findMedianSortedArrays(self, A, B):
        l = len(A) + len(B)
        return self.findKth(A, B, l // 2) if l % 2 == 1 else (self.findKth(A, B, l // 2 - 1) + self.findKth(A, B, l // 2)) / 2.0

    def findKth(self, A, B, k):
        if len(A) > len(B):
            A, B = B, A
        if not A:
            return B[k]
        if k == len(A) + len(B) - 1:
            return max(A[-1], B[-1])
        i = len(A) // 2
        j = k - i
        if A[i] > B[j]:
            # Here I assume it is O(1) to get A[:i] and B[j:]. In python, it's
            # not but in cpp it is.
            return self.findKth(A[:i], B[j:], i)
        else:
            return self.findKth(A[i:], B[:j], j)

# O(log(min(m,n))
# https://discuss.leetcode.com/topic/4996/share-my-o-log-min-m-n-solution-with-explanation
# 总耗时: > 600ms


class Solution6:
    # @return a float

    def findMedianSortedArrays(self, A, B):
        m, n = len(A), len(B)
        if m > n:
            A, B, m, n = B, A, n, m
        if n == 0:
            raise ValueError

        imin, imax, half_len = 0, m, (m + n + 1) // 2
        while imin <= imax:
            i = (imin + imax) // 2
            j = half_len - i
            if i < m and B[j - 1] > A[i]:
                # i is too small, must increase it
                imin = i + 1
            elif i > 0 and A[i - 1] > B[j]:
                # i is too big, must decrease it
                imax = i - 1
            else:
                # i is perfect

                if i == 0:
                    max_of_left = B[j - 1]
                elif j == 0:
                    max_of_left = A[i - 1]
                else:
                    max_of_left = max(A[i - 1], B[j - 1])

                if (m + n) % 2 == 1:
                    return max_of_left

                if i == m:
                    min_of_right = B[j]
                elif j == n:
                    min_of_right = A[i]
                else:
                    min_of_right = min(A[i], B[j])

                return (max_of_left + min_of_right) / 2.0


class Solution7:
    """
    @param: A: An integer array
    @param: B: An integer array
    @return: a double whose format is *.5 or *.0
    """

    def findMedianSortedArrays(self, A, B):
        # write your code here
        length_a = len(A)
        length_b = len(B)
# 总耗时: 555 ms


class Solution8:
    # @return a float

    def findMedianSortedArrays(self, A, B):
        l = len(A) + len(B)
        if l % 2 == 1:
            return self.findKth(A, B, l // 2)
        else:
            return (self.findKth(A, B, l // 2 - 1) +
                    self.findKth(A, B, l // 2)) / 2

    def findKth(self, A, B, k):
        if len(A) > len(B):
            A, B = B, A
        if not A:
            return B[k]
        if k == len(A) + len(B) - 1:
            return max(A[-1], B[-1])
        i = len(A) // 2
        j = k - i
        if A[i] > B[j]:
            # Here I assume it is O(1) to get A[:i] and B[j:]. In python, it's
            # not but in cpp it is.
            return self.findKth(A[:i], B[j:], i)
        else:
            return self.findKth(A[i:], B[:j], j)


if __name__ == '__main__':
    s = Solution6()
    # [1, 1, 2, 2, 3]
    # print(s.medianII([1, 2, 3, 4, 5]))
    # [4, 4, 4, 3, 3, 3, 3]
    # print(s.medianII([4, 5, 1, 3, 2, 6, 0]))
    # [2, 2, 20]
    # print(s.medianII([2, 20, 100]))
    # print(s.median([4, 5, 1, 2, 3]))
    # print(s.median(nums=[1, 2, 3, 4, 5, 6, 7, 100, 200, 1000]))
    # A = [
    #     595240, 373125, 463748, 417209, 209393, 747977, 864346, 419023, 925673,
    #     307640, 597868, 833339, 130763, 814627, 766415, 79576, 459038, 990103,
    #     944521, 708820, 473246, 499960, 742286, 758503, 270229, 991199, 770718,
    #     529265, 498975, 721068, 727348, 29619, 712557, 724373, 823743, 318203,
    #     290432, 476213, 412181, 869308, 496482, 793858, 676162, 165869, 160511,
    #     260864, 502521, 611678, 786798, 356560, 916620, 922168, 89350, 857183,
    #     964051, 979979, 916565, 186532, 905289, 653307, 351329, 195491, 866281,
    #     183964, 650765, 675046, 661642, 578936, 78684, 50105, 688326, 648786,
    #     645823, 652329, 961553, 381367, 506439, 77735, 707959, 373271, 316194,
    #     185079, 686945, 342608, 980794, 78777, 687520, 27772, 711098, 661265,
    #     167824, 688245, 286419, 400823, 198119, 35400, 916784, 81169, 874377,
    #     377128, 922531, 866135, 319912, 867697, 10904]
    # k = 105
    # print(s.kthLargestElement(k, A))
    A = [1, 2, 3, 4, 5, 6]
    B = [2, 3, 4, 5]
    result = s.findMedianSortedArrays(A, B)
    print(result)
