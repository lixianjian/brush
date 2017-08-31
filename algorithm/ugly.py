#!/usr/bin/env /usr/local/bin/python3
# -*- coding: utf-8 -*-
'''
Created on 2017年8月29日

@author: lixianjian
'''

# >mk, m=第n个超级丑数的值
class Solution(object):

    def isUgly(self, num, primes=[2, 3, 5]):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        for x in primes:
            while num % x == 0:
                num = num // x
                if num == 1:
                    return True
        return False

    def nthSuperUglyNumber(self, n, primes):
        """
        @param: n: a positive integer
        @param: primes: the given prime list
        @return: the nth super ugly number
        """
        # write your code here
        num = 1
        if n > 1:
            while n - 1:
                num += 1
                if self.isUgly(num, primes):
                    n -= 1
                    print(num)
        return num


import heapq
from copy import copy
class Solution2(object):

    def isUgly(self, num, primes=[2, 3, 5]):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        for x in primes:
            while num % x == 0:
                num = num // x
                if num == 1:
                    return True
        return False

    def nthSuperUglyNumber(self, n, primes):
        """
        @param: n: a positive integer
        @param: primes: the given prime list
        @return: the nth super ugly number
        """
        # write your code here
        num = 1
        if n > 1:
            primes.sort()
            heap = copy(primes)
            heapq.heapify(heap)
            while n - 1:
                num = heapq.heappop(heap)
                for x in primes:
                    if num < primes[-1] and x < num:
                        continue
                    heapq.heappush(heap, num * x)
                print(num, heap)
                n -= 1
        return num


class Solution3(object):
    def nthSuperUglyNumber(self, n, primes):
        uglies = [1]
        def gen(prime):
            for ugly in uglies:
                yield ugly * prime
        merged = heapq.merge(*map(gen, primes))
        while len(uglies) < n:
            ugly = next(merged)
            if ugly != uglies[-1]:
                uglies.append(ugly)
        return uglies[-1]

import itertools
class Solution4(object):
    def nthSuperUglyNumber(self, n, primes):
        uglies = [1]
        merged = heapq.merge(*map(lambda p: (u*p for u in uglies), primes))
        uniqed = (u for u, _ in itertools.groupby(merged))
        map(uglies.append, itertools.islice(uniqed, n-1))
        return uglies[-1]

# 总耗时: 1435 ms
class Solution5(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        ugly = [1] * n
        length = len(primes)
        # 保存与相同索引位置的质数相乘的最后一个丑数的位置
        i_list = [-1] * length
        # 保存相同索引位置的质数对应的最小丑数
        v_list = [1] * length

        for k in range(n):
            x = min(v_list)
            ugly[k] = x
            # 索引位置质数对应的丑数是最小值，则计算该质数对应的下一个最小值
            for i in range(length):
                if x == v_list[i]:
                    # 索引位置质数对应的丑数是最小值，则计算该质数对应的下一个最小值
                    i_list[i] += 1
                    v_list[i] = ugly[i_list[i]] * primes[i]
        return ugly[-1]

class Solution6(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        nums=[1]*len(primes)
        idx=[0]*len(primes)
        best=[1]
        cur=1
        for i in range(n-1):
            for j in range(len(idx)):
                if nums[j]==cur:
                    nums[j]=best[idx[j]]*primes[j]
                    idx[j]+=1
            cur=min(nums)
            best.append(cur)
        return best[-1]

if __name__ == '__main__':

    s = Solution6()
    # print('8:', s.isUgly(8))
    # print('14:', s.isUgly(14))
    print(s.nthSuperUglyNumber(12, primes=[2, 7, 13, 19]))
    # print(s.nthSuperUglyNumber(41, primes=[103, 59, 139, 197, 73]))
