#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/6/2 14:43
# @Author  : ChenSir
# @File    : Life.py
# @Software: PyCharm

# -*- encoding: utf-8 -*-


SCORE_NONE = -1


class Life(object):
    """个体类"""

    def __init__(self, aGene=None):
        self.gene = aGene
        self.score = SCORE_NONE
