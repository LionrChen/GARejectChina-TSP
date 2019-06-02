#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/6/2 14:43
# @Author  : ChenSir
# @File    : TSP_GA.py
# @Software: PyCharm

# -*- encoding: utf-8 -*-

import math
from GA import GA


class TSP(object):
    def __init__(self, aLifeCount=100, ):
        self.initCitys()
        self.lifeCount = aLifeCount
        self.ga = GA(aCrossRate=0.7,
                     aMutationRate=0.02,
                     aLifeCount=self.lifeCount,
                     aGeneLength=len(self.citys),
                     aMatchFun=self.matchFun())

    def initCitys(self):
        self.citys = []
        f = open("distanceMatrix.txt", "r", encoding='utf-8')
        while True:
            # 一行一行读取
            loci = str(f.readline())
            if loci:
                pass  # do something here
            else:
                break
            # 用readline读取末尾总会有一个回车，用replace函数删除这个回车
            loci = loci.replace("\n", "")
            # 按照tab键分割
            loci = loci.split("\t")
            # 中国34城市经纬度读入citys
            self.citys.append((float(loci[1]), float(loci[2]), loci[0]))

    # order是遍历所有城市的一组序列，如[1,2,3,7,6,5,4,8……]
    # distance就是计算这样走要走多长的路
    def distance(self, order):
        distance = 0.0
        # i从-1到32,-1是倒数第一个
        for i in range(-1, len(self.citys) - 1):
            index1, index2 = order[i], order[i + 1]
            city1, city2 = self.citys[index1], self.citys[index2]
            distance += math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

        return distance

    def haversine(self, order):  # 经度1，纬度1，经度2，纬度2 （十进制度数）
        """
        Calculate the great circle distance between two points
        on the earth (specified in decimal degrees)
        """
        distance = 0.0
        # i从-1到32,-1是倒数第一个
        for i in range(-1, len(self.citys) - 1):
            index1, index2 = order[i], order[i + 1]
            city1, city2 = self.citys[index1], self.citys[index2]
            lon1, lat1, lon2, lat2 = map(math.radians, [city1[0], city1[1], city2[0], city2[1]])
            # haversine公式
            dlon = lon2 - lon1
            dlat = lat2 - lat1
            a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
            c = 2 * math.asin(math.sqrt(a))
            r = 6371  # 地球平均半径，单位为公里
            distance += c * r * 1000
        return distance

    # 适应度函数，因为我们要从种群中挑选距离最短的，作为最优解，所以（1/距离）最长的就是我们要求的
    def matchFun(self):
        return lambda life: 1.0 / self.distance(life.gene)

    def run(self, n=0):
        while n > 0:
            self.ga.next()
            distance = self.haversine(self.ga.best.gene)
            print(("%d : %f公里") % (self.ga.generation, distance/1000), "Bast Gene:", self.ga.best.gene)
            n -= 1
        print("经过%d次迭代，最优解距离为：%f" % (self.ga.generation, distance/1000))
        print("遍历城市顺序为：",)
        # print "遍历城市顺序为：", self.ga.best.gene
        # 打印出我们挑选出的这个序列中
        for i in self.ga.best.gene:
            print(self.citys[i][2])


def main():
    tsp = TSP()
    tsp.run(10000)


if __name__ == '__main__':
    main()