from partition import *
from pyexcel_ods import save_data
import collections

data_vec = [['Grupo', 'd1', 'd2']]
coordinates = Coordinate.coordinates_from_file('../datasets/monkey.txt')
partitions = Partition.partitions_from_file('results/monkey/k_medias/monkey_k_medias_7_clusters.txt')
for i in range(len(partitions)):
    data_vec.append([partitions[i], coordinates[i].d1, coordinates[i].d2])
data = collections.OrderedDict()
data.update({"Planilha 1": data_vec})
save_data('monkey_k_medias_7_clusters.ods', data)
