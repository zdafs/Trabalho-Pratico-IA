# -*- coding: UTF-8 -*-

from coordinate import *
import random

class Partition(object):
    """docstring for Partition"""
    def __init__(self, nk):
        self.nk = nk

    @staticmethod
    def initialize(coordinates):
        partitions = []
        i = 0
        for coordinate in coordinates:
            coordinate.partition = i
            i += 1
            partitions.append(Partition(1))
        return partitions

    @staticmethod
    def partitions_to_file(coordinates, file_name):
        file = open(file_name, 'w')

        for coordinate in coordinates:
            file.write(coordinate.label+' '+str(coordinate.partition)+'\n')

        file.close()
