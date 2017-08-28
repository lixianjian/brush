# !/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Created on 2017年8月18日

@author: lixianjian
'''


class Solution:
    """
    @param: board: the board
    @return: whether the Sudoku is valid
    """

    def isValidSudoku(self, board):
        # write your code here
        # h
        for b in board:
            h = []
            for value in b:
                if value == u'.':
                    continue
                if value in h:
                    return False
                h.append(value)

        # v
        for i in range(9):
            v = []
            for b in board:
                value = b[i]
                if value == u'.':
                    continue
                if value in v:
                    return False
                v.append(value)

        i = 0
        for k in range(3):
            # 大宫格3行
            im = i + (k + 1) * 3
            j = 0
            for m in range(3):
                l = []
                jm = j + (m + 1) * 3
                # indexs.append((im, jm))
                for vi in range(jm - 3, jm):
                    for hi in range(im - 3, im):
                        value = board[hi][vi]
                        if value == u'.':
                            continue
                        if value in l:
                            return False
                        l.append(value)

        return True


def get_indexs():

    indexs = []
    i = 0
    for k in range(3):
        # 大宫格3行
        im = i + (k + 1) * 3
        j = 0
        for m in range(3):
            jm = j + (m + 1) * 3
            indexs.append((im, jm))
    print(indexs)

if __name__ == '__main__':

    board = ["....5..1.",
             ".4.3.....",
             ".....3..1",
             "8......2.",
             "..2.7....",
             ".15......",
             ".....2...",
             ".2.9.....",
             "..4......"]
    s = Solution()
    result = s.isValidSudoku(board)
    print(result)

    # get_indexs()
