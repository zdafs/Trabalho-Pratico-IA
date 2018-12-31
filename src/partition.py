# -*- coding: UTF-8 -*-

from coordinate import *
import helper
import random

class Partition(object):
    """docstring for Partition"""
    def __init__(self, centroide, nk):
        self.centroide = centroide
        self.nk = nk

    @staticmethod
    def initialize(coordinates, k):
        random.seed()
        coordinate_sample = random.sample(coordinates, k)
        partitions = []
        for centroide in coordinate_sample:
            partitions.append(Partition(Coordinate(centroide.d1, centroide.d2), 0))
        return partitions

    @staticmethod
    def partitions_to_file(coordinates, file_name):
        file = open(file_name, 'w')

        for coordinate in coordinates:
            file.write(coordinate.label+' '+str(coordinate.partition)+'\n')

        file.close()

    @staticmethod
    def partitions_from_file(file_name):
        partitions = []
        file = open(file_name, 'r')

        for line in file:
            partition = re.split(' |\t', line)
            partitions.append(int(partition[1]))

        file.close()
        return partitions

    @staticmethod
    def adjusted_rand_index(partition_1, partition_2, start_index_p1_is_0, start_index_p2_is_0):
        k_1, k_2 = max(partition_1), max(partition_2)
        add1, add2 = 1, 1

        if start_index_p1_is_0:
            add1 = 0
            k_1+=1
        if start_index_p1_is_0:
            add2 = 0
            k_2+=1

        cont_table = [[0 for j in range(k_2)] for i in range(k_1)]
        sum_col = [0 for i in range(k_2)]
        sum_row = [0 for i in range(k_1)]

        for i in range(len(partition_1)):
            p1, p2 = partition_1[i]-add1, partition_2[i]-add2

            cont_table[p1][p2] =  cont_table[p1][p2]+1
            sum_row[p1] = sum_row[p1]+1
            sum_col[p2] = sum_col[p2]+1

        sum_nij = 0.0
        for i in range(k_1):
            for j in range(k_2):
                sum_nij += helper.binomial_coefficient(cont_table[i][j], 2)

        sum_ai = 0.0
        for i in range(k_1):
            sum_ai += helper.binomial_coefficient(sum_row[i], 2)

        sum_bj = 0.0
        for i in range(k_2):
            sum_bj += helper.binomial_coefficient(sum_col[i], 2)

        return (sum_nij - ((sum_ai*sum_bj)/helper.binomial_coefficient(len(partition_1), 2)))/((sum_ai+sum_bj)/2 - (sum_ai*sum_bj)/helper.binomial_coefficient(len(partition_1), 2))
