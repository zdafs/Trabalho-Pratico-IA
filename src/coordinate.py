# -*- coding: UTF-8 -*-

import re
import math

class Coordinate(object):
    """docstring for Coordinate"""
    def __init__(self, d1, d2, label=''):
        self.label = label
        self.d1 = d1
        self.d2 = d2

    @staticmethod
    def coordinates_from_file(file_name):
        coordinates = []
        file = open(file_name, 'r')

        file.readline()
        for line in file:
            coordinate = re.split(' |\t', line)
            coordinates.append(Coordinate(float(coordinate[1]), float(coordinate[2]), coordinate[0]))
        file.close()

        return coordinates

    @staticmethod
    def euclidean_distance(p1, p2):
        return math.sqrt((p1.d1-p2.d1)**2 + (p1.d2-p2.d2)**2)
