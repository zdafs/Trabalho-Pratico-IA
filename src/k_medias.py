# -*- coding: UTF-8 -*-

import sys
import os
from partition import *

def associa_objeto(coordinate, partitions):
    minimo = Coordinate.euclidean_distance(coordinate, partitions[0].centroide)
    min_index = 0

    for i in range(1, len(partitions)):
        aux = Coordinate.euclidean_distance(coordinate, partitions[i].centroide)
        if minimo > aux:
            minimo = aux
            min_index = i

    coordinate.partition = min_index + 1
    partitions[min_index].nk += 1

def recalcula_centroides(coordinates, partitions):
    res_partitions = [Partition(Coordinate(0, 0), 0) for i in range(0, len(partitions))]
    for coordinate in coordinates:
        res_partitions[coordinate.partition-1].centroide.d1 += coordinate.d1
        res_partitions[coordinate.partition-1].centroide.d2 += coordinate.d2
    for i in range(0, len(partitions)):
        res_partitions[i].centroide.d1 /= partitions[i].nk
        res_partitions[i].centroide.d2 /= partitions[i].nk

    return res_partitions

file_name = sys.argv[1]
k = int(sys.argv[2])
it = int(sys.argv[3])

coordinates = Coordinate.coordinates_from_file(file_name)

partitions = Partition.initialize(coordinates, k)

for i in range(0, it):
    for coordinate in coordinates:
        associa_objeto(coordinate, partitions)
    partitions = recalcula_centroides(coordinates, partitions)

file = os.path.splitext(os.path.basename(file_name))

Partition.partitions_to_file(coordinates, file[0]+'_k_medias_'+str(k)+'_clusters'+file[1])
