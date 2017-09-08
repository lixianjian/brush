# !/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Created on 2017年8月18日

@author: lixianjian
'''

from copy import copy

"""
Definition of TreeNode:
"""


class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

    def add_child_left(self, node=None):
        self.left = node

    def add_child_right(self, node=None):
        self.right = node


def add_node(root, elem, nodes=[]):
    node = TreeNode(elem)

    if node:
        nodes.append(node)
    if root.left is None:
        root.left = node
    else:
        root.right = node
        nodes.pop(0)


def preorder(root):  # 前序遍历
    if root is None:
        return
    else:
        print(root.val)
        preorder(root.left)
        preorder(root.right)


def level_queue(root):
    """利用队列实现树的层次遍历"""
    if root is None:
        return
    myQueue = []
    node = root
    myQueue.append((node, 'root', 0))
    while myQueue:
        node, prefix, parent = myQueue.pop(0)
        print(node.val, prefix, parent)
        if node.left is not None:
            myQueue.append((node.left, 'left', node.val))
        if node.right is not None:
            myQueue.append((node.right, 'right', node.val))


class Solution:
    # @param {TreeNode} root the root of binary tree
    # @param {int} target an integer
    # @return {int[][]} all valid paths

    def __init__(self):
        self.result = []
        self.target = 0

    def binaryTreePathSum(self, root, target):
        # Write your code here
        self.target = target

        if root:
            self.value_sum(root, count=0, l=[])

        return self.result

    def value_sum(self, root, count, l):
        l.append(root.val)
        count += root.val
        if root.left is None and root.right is None:
            # print(root.val, count, l)
            if count == self.target:
                self.result.append(l)
            return

        if root.left:
            lleft = copy(l)
            self.value_sum(root.left, count, lleft)

        if root.right:
            lright = copy(l)
            self.value_sum(root.right, count, lright)


# 给定一个二叉树,确定它是高度平衡的。对于这个问题,一棵高度平衡的二叉树的定义是：一棵二叉树中每个节点的两个子树的深度相差不会超过1。
# 总耗时: 1586 ms

class Solution2:
    """
    @param: root: The root of binary tree.
    @return: True if this Binary tree is Balanced, or false.
    """

    def isBalanced(self, root):
        # write your code here
        if not root:
            return True

        return abs(self.get_height(root.left) -
                   self.get_height(root.right)) < 2 and \
            self.isBalanced(root.left) and self.isBalanced(root.right)

    def get_height(self, node):
        if not node:
            return 0

        return 1 + max(self.get_height(node.left), self.get_height(node.right))


# 二叉树的最大深度
# 给定一个二叉树，找出其最大深度。
# 二叉树的深度为根节点到最远叶子节点的距离。
# 总耗时: 872 ms
class Solution3:
    """
    @param root: The root of binary tree.
    @return: An integer
    """

    def maxDepth(self, root):
        # write your code here
        if not root:
            return 0

        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

if __name__ == '__main__':
    # elems = ['a', 'b', 'c', 'd', 'e', 'f']
    # 5, [[1, 2, 2], [1, 4]]
    # elems = [1, 2, 4, 2, 3]
    # target = 5
    # -31 [[37,-48,48,-54,-22,8]]
    # elems = [37, -34, -48, 0, -100, -100, 48, 0, 0,
    #          0, 0, -54, 0, -71, -22, 0, 0, 0, 8]
    # target = -31
    # root = TreeNode(elems[0])
    # nodes = [root]
    # for elem in elems[1:]:
    #     i = 0
    #     for node in nodes:
    #         if nodes[i].val is not 0:
    #             break
    #         i += 1

    #     nodes = nodes[i:]
    #     add_node(nodes[0], elem, nodes)
    #     # print(root.val, root.left.val, root.right.val)
    # # preorder(root)
    # level_queue(root)

    # s = Solution()
    # result = s.binaryTreePathSum(root, target)
    # print(result)

    elems = [3, 9, 20, 0, 0, 15, 7]
    # elems = [3, 0, 20, 15, 7]
    root = TreeNode(1)
    node2 = TreeNode(2)
    root.right = node2
    node3 = TreeNode(3)
    node2.left = node3
    s = Solution2()
    result = s.isBalanced(root)
    print(result)
