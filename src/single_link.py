# -*- coding: UTF-8 -*-

import sys
import os
from partition_SL import *

def junta_part(coordinates, partitions):
    min_dist = Coordinate.euclidean_distance(coordinates[0], coordinates[1])
    part1 = coordinates[0].partition
    part2 = coordinates[1].partition

    for i in range(0, len(coordinates)):
        for j in range(0, i):
            if coordinates[i].partition != coordinates[j].partition:
                aux = Coordinate.euclidean_distance(coordinates[i], coordinates[j])
                if aux < min_dist:
                    min_dist = aux
                    part1 = coordinates[i].partition
                    part2 = coordinates[j].partition

    print str(min_dist) + ' ' + str(part1) + ' ' + str(part2) + '\n'
    for coordinate in coordinates:
        if coordinate.partition == part1:
            coordinate.partition = part2
            partitions[part2].nk += 1
        if coordinate.partition > part1:
            coordinate.partition -= 1;

    partitions.pop(part1)

file_name = sys.argv[1]
kmin = int(sys.argv[2])
kmax = int(sys.argv[3])

coordinates = Coordinate.coordinates_from_file(file_name)

partitions = Partition.initialize(coordinates)

for i in range(len(partitions)-1, kmin-1, -1):
    junta_part(coordinates, partitions)
    print 'Executando' + ' ' + str(i) + '\n'
    if i <= kmax:
        file = os.path.splitext(os.path.basename(file_name))
        Partition.partitions_to_file(coordinates, file[0]+'_single_link_'+str(i)+'_clusters'+file[1])
