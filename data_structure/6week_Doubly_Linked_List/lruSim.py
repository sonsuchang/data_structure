import os
from circularDoublyLinkedList import *
print(os.getcwd())
currentPath = os.getcwd()
os.chdir(currentPath+"\data_structure\Doubly_Linked_List")
print(os.getcwd())
'''
def do_sim(cache_slots):

    cache_hit = 0
    tot_cnt = 0 #cache_hit + cache_miss
    data_file = open("linkbench_short.trc")
    for line in data_file.readlines():
        lpn = line.split()[0]

    # do programming here!

    #print("cache_slot = ", cache_slots, "cache_hit = ", cache_hit, "hit ratio = ", cache_hit / tot_cnt)

if __name__ == "__main__":

    for cache_slots in range(100, 1000, 100):
        do_sim(cache_slots)
'''