#!/usr/bin/env /usr/local/bin/python3
# -*- coding: utf-8 -*-
'''
Created on 2017年8月27日

@author: lixianjian
'''
from copy import copy


"""
Definition of ListNode
"""


class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

# 406ms
from operator import attrgetter


class Solution:
    # @param a list of ListNode
    # @return a ListNode

    def mergeKLists(self, lists):
        sorted_list = []
        for head in lists:
            curr = head
            while curr is not None:
                sorted_list.append(curr)
                curr = curr.next

        sorted_list = sorted(sorted_list, key=attrgetter('val'))
        for i, node in enumerate(sorted_list):
            try:
                node.next = sorted_list[i + 1]
            except:
                node.next = None

        if sorted_list:
            return sorted_list[0]
        else:
            return None

import heapq


class Solution2:

    def mergeKLists(self, lists):

        ret, heap = [], []
        for lst in lists:
            while lst:
                heapq.heappush(heap, lst.val)
                lst = lst.next

        while heap:
            ret.append(heapq.heappop(heap))
        if ret:
            return ret[0]

        return None

# 577 ms


class Solution3:

    def mergeKLists(self, lists):

        def merge(lst1, lst2):
            dummy = pt = ListNode(-1)
            while lst1 and lst2:
                if lst1.val < lst2.val:
                    pt.next = lst1
                    lst1 = lst1.next
                else:
                    pt.next = lst2
                    lst2 = lst2.next
                pt = pt.next

            pt.next = lst1 if not lst2 else lst2
            return dummy.next

        if not lists:
            return None

        if len(lists) == 1:
            return lists[0]
        mid = len(lists) / 2
        left = self.mergeKLists(lists[:mid])
        right = self.mergeKLists(lists[mid:])

        return merge(left, right)

# 491 ms
from heapq import heappush, heappop, heapreplace, heapify


class Solution4:

    def mergeKLists(self, lists):

        dummy = node = ListNode(0)
        h = [(n.val, n) for n in lists if n]
        heapify(h)
        while h:
            v, n = h[0]
            if n.next is None:
                heappop(h)  # only change heap size when necessary
            else:
                heapreplace(h, (n.next.val, n.next))
            node.next = n
            node = node.next

        return dummy.next


def init_nodes(l=[]):
    top = None
    if not l:
        return top

    top = ListNode(val=l[0])
    pre_node = top
    for e in l[1:]:
        node = ListNode(val=e)
        pre_node.next = node
        pre_node = node
    return top


def print_node(node):
    result = [node.val]
    while node.next is not None:
        result.append(node.next.val)
        node = node.next
    print(result)


if __name__ == '__main__':
    num_list = []
    nodes = []
    for l in num_list:
        nodes.append(init_nodes(l))

    s = Solution()
    print_node(s.mergeKLists(nodes))
