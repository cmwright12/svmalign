from makedataset_letters import *
from scoringfunction import *
import random

num_natives = 1
num_decoys = 3
native_set = []
hom_set = []
decoy_set = []

def make_natives():
    for i in range(num_natives):
        native_set.append(make_native_sequence())

def make_decoy():
    seq = ''
    for i in range(len_N):
        seq += random.choice(pool)
    return seq
        
def make_homs():
    for n in native_set:
        hom_set.append(make_hom(n))
        
def make_decoys():
    for n in native_set:
        SD = []
        for i in range(num_decoys):
            SD.append(make_decoy())
        decoy_set.append(SD)
        
make_natives()
make_homs()
make_decoys()

"""
print "\n\nNatives:"
for n in native_set:
    print n
print "\n\nHomologs:"
for h in hom_set:
    print h
print "\n\nDecoys:"
for d in decoy_set:
    print d
"""

def get_collection(sample_num):
    index = sample_num - 1
    collection = {"index": sample_num, "native": native_set[index], "hom": hom_set[index], "decoys": decoy_set[index]}
    return collection

sample1 = get_collection(1)
for key, value in sample1.iteritems():
    print key, value
    
    
#s1, s2 = aligns(native_set[0], hom_set[0])
#align = make_align(s1,s2)
#print "Features: ", fa(s1,s2,align)