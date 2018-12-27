# -*- coding: UTF-8 -*-

import sys
import os
from partition_SL import *

def inicializaDist(coordinates):
    matriz = []
    for i in range(len(coordinates)):
        linha = []
        for j in range(i+1):
            if i == j:
                list.append(linha, 0)
            else:
                list.append(linha,Coordinate.euclidean_distance(coordinates[i], coordinates[j]))
        matriz = matriz + [linha]
    return matriz

def recalculaDist(dist, part1, part2, partitions):
    i = 0
    while i < part2:
        dist[part2][i] = ((partitions[part2].nk*dist[part2][i])+(partitions[part1].nk*dist[part1][i]))
        dist[part2][i] = dist[part2][i]/(partitions[part1].nk+partitions[part2].nk)
        i+=1
    i+=1
    while i < part1:
        dist[i][part2] = ((partitions[part2].nk*dist[i][part2])+(partitions[part1].nk*dist[part1][i]))
        dist[i][part2] = dist[i][part2]/(partitions[part1].nk+partitions[part2].nk)
        i+=1
    i+=1
    while i < len(partitions):
        dist[i][part2] = ((partitions[part2].nk*dist[i][part2])+(partitions[part1].nk*dist[i][part1]))
        dist[i][part2] = dist[i][part2]/(partitions[part1].nk+partitions[part2].nk)
        i+=1
    for j in range(len(partitions)-1, part1, -1):
        dist[j].pop(part1)
    dist.pop(part1)
    return dist

def junta_part(coordinates, partitions, dist):
    min_dist = dist[1][0]
    part1 = 1
    part2 = 0

    for i in range(1, len(partitions)):
        for j in range(0, i):
            if dist[i][j] < min_dist:
                min_dist = dist[i][j]
                part1 = i
                part2 = j

    dist = recalculaDist(dist, part1, part2, partitions)
    for coordinate in coordinates:
        if coordinate.partition == part1:
            coordinate.partition = part2
        if coordinate.partition > part1:
            coordinate.partition -= 1
    partitions[part2].nk += partitions[part1].nk
    partitions.pop(part1)
    return dist

file_name = sys.argv[1]
kmin = int(sys.argv[2])
kmax = int(sys.argv[3])

coordinates = Coordinate.coordinates_from_file(file_name)

partitions = Partition.initialize(coordinates)

dist = inicializaDist(coordinates)

for i in range(len(partitions)-1, kmin-1, -1):
    dist = junta_part(coordinates, partitions, dist)
    #print 'Executando' + ' ' + str(i) + '\n'
    if i <= kmax:
        file = os.path.splitext(os.path.basename(file_name))
        Partition.partitions_to_file(coordinates, file[0]+'_average_link_'+str(i)+'_clusters'+file[1])
