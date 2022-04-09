import os
from circularDoublyLinkedList import *
currentPath = os.getcwd()
os.chdir(currentPath+"\data_structure\\Doubly_Linked_List")

def do_sim(cache_slots):

    cache_hit = 0
    tot_cnt = 0 #cache_hit + cache_miss
    data_file = open("linkbench_short.trc")
    cache_list = CircularDoublyLinkedList()
    for line in data_file.readlines():
        lpn = line.split()[0]
        if cache_list.size() >= cache_slots:
            if cache_list.count(lpn) > 0:
                cache_hit += 1
                tot_cnt += 1
                cache_list.remove(lpn)
                cache_list.append(lpn)
            else:
                tot_cnt += 1
                cache_list.pop(0)
                cache_list.append(lpn)
        else:
            if cache_list.count(lpn) > 0:
                cache_hit += 1
                tot_cnt += 1
                cache_list.remove(lpn)
                cache_list.append(lpn)
            else:
                tot_cnt += 1
                cache_list.append(lpn)
    print("cache_slot = ", cache_slots, "cache_hit = ", cache_hit, "hit ratio = ", cache_hit / tot_cnt)

if __name__ == "__main__":

    for cache_slots in range(100, 1100, 100):
        do_sim(cache_slots)