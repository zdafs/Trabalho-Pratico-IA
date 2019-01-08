from partition import *
from pyexcel_ods import save_data
import collections

data_vec = [['Grupo', 'd1', 'd2']]
coordinates = Coordinate.coordinates_from_file('../datasets/c2ds1-2sp.txt')
partitions = Partition.partitions_from_file('results/c2ds1-2sp/k_medias/c2ds1-2sp_k_medias_4_clusters.txt')
for i in range(len(partitions)):
    data_vec.append([partitions[i], coordinates[i].d1, coordinates[i].d2])
data = collections.OrderedDict()
data.update({"Planilha 1": data_vec})
save_data('c2ds1-2sp_k_medias_4_clusters.ods', data)
