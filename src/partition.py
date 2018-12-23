# -*- coding: UTF-8 -*-

from coordinate import *
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
