from partition import *
file = open('monkey_rand_single_link.txt', 'w')
partition_2 = Partition.partitions_from_file('../datasets/monkeyReal1.clu')
for i in range(5, 13):
    file_name = 'results/monkey/single_link/monkey_single_link_'+str(i)+'_clusters.txt'
    partition_1 = Partition.partitions_from_file(file_name)
    rand_index = Partition.adjusted_rand_index(partition_1, partition_2, True, False)
    file.write(str(i)+' - '+str(rand_index) + '\n')
file.close()
