# I ADDED THIS LINE
# AND THIS ONE
#python numpy: tensordot

import random
import numpy as np
import matplotlib.pyplot as plt
from Bio import pairwise2
from Bio.pairwise2 import format_alignment
from alphanum import *

# returns pool = [1,2,2,3,3,3,...20x20]
def make_pool():
    alphabet = range(1,21)
    pool = []
    for item in alphabet:
        for count in range(item):
            pool.append(item)
    return pool

# returns a sequence of given length with elements randomly chosen from a given set/bucket 
def make_sequence(bucket, length):
    new_seq = []
    for i in range(length):
        new_seq.append(random.choice(bucket))
    return new_seq

def make_native(seq_len):
    #for i in range(num_natives):
    #    natives.append(make_sequence(pool, seq_len))
    native = make_sequence(pool, seq_len)
    return native

def make_alignment_list(align_seq_len):
    #align_seq = []
    align_pool = ['m', 'm', 'm','m','s','s', 'i', 'i', 'd', 'd']
    #align_seq_len = 10
    #for i in range():
    #    new_aseq = make_sequence(align_pool, align_seq_len)
    #    alists.append(new_aseq)
    align_seq = make_sequence(align_pool, align_seq_len)
    return align_seq
        
def make_sublist(native, align):
    """
    max_start = len(list) - min_len - 1
    start = random.randrange(0,max_start)
    #length = random.randrange(min_len, len(list)-start)
    
    sub = list[start:start+length]
    begin = sub[0:start]
    #end =
    return sub"""
    
    diff = len(native) - len(align)
    start = random.randrange(0, diff)
    if len(align) < diff:
        length = random.randrange(len(align), diff)
    else:
        length = random.randrange(diff, len(align))
    stop = start + length
    sublist = native[start:stop]
    
    return sublist

def apply_align(align, sub):
    #print "Sub0:   ", sub
    index = 0
    hom = list(sub)
    for a in align:
        #print "Sublist: ", sub, ", a: ", a, ", Index: ", index
        if a == 's':
            hom[index] = (sub[index] - 1) % 20
            index += 1
            #print 's', index
        elif a == 'm':
            index += 1
            #print 'm', index
        elif a == 'i':
            hom.insert(index,random.choice(pool))
            index += 1
            #print 'i', index
        elif a == 'd':
            del hom[index]
            #hom.insert(index,0)
            #print 'd', index
        
    #print "Hom1:   ", hom
    #return pad(sub,pool)
    return hom
    
def make_hom(natv, aln):
    print "Running make_sub..."
    n = len(natv)
    seq_length = len(aln)
    start = random.randrange(0,n-seq_length)
    stop = random.randrange(start+seq_length,n)
    begin = natv[0:start]
    end = natv[stop:n]
    #print start, stop, stop-start

    sub = natv[start:stop]
    hom = apply_align(aln, sub)
    return begin + hom + end
      
# pads beginning and end of list with random characters
def pad(mylist,elementset):
    max_extra = 3
    begin = random.sample(elementset, random.randrange(1,max_extra))
    end = random.sample(elementset, random.randrange(1,max_extra))
    mylist.extend(end)
    mylist.reverse()
    mylist.extend(begin)
    mylist.reverse()
    return mylist
    
def aligns(s1,s2):
    print("local: match = 3, mismatch = -1, gap = -2")
    for a in pairwise2.align.localms(s1,s2,3,-1,-2,-2):
        print(format_alignment(*a))
        
def test1():
    native = [5,2,9,2,1,3,5,5,2,1,9,2,1]
    align = ['m', 'm', 's', 'm', 'm', 'i', 'm', 'm']
    align_count = [align.count('d'), align.count('i'), align.count('m'), align.count('s')]
    wscore = [-2, -2, 3, -1]
    align_score = np.dot(align_count, wscore)

    sub = [2,1,3,5,5,2,1]
    
    print "Native: ", native
    print "Align:  ", align
    print "Sub:    ", sub
    
    hom1 = make_hom(native, align)
    hom = [3,2,1,2,5,5,3,2,1,4,7,6,5,2]
    #hom = [2,1,2,5,5,3,2,1]    
    print "Hom0    ", hom
    print "Homp1   ", hom1

    num_decoys = 10
    decoys = []
    decoy_seq_len = len(native)
    
    #for i in range(num_decoys):
    #    decoys.append(make_sequence(pool,decoy_seq_len))
    #print "Decoys: ", len(decoys)
    
    print "Align score: ", align_score, align_count, wscore
    aligns(lst2str(native), lst2str(hom1))
 
def test2():
    #native = make_native_sequence(10)
    #native = [15, 13, 15, 20, 18, 8, 9, 17, 19, 20]
    native = [5,2,9,2,1,3,5,5,2,1,9,2,1]
    #align = make_alignment_list(6)
    align = ['d', 's', 'd', 'i', 'i', 'm']
    #align = ['m', 'm', 's', 'm', 'm', 'i', 'm', 'm']
    
    align_count = [align.count('d'), align.count('i'), align.count('m'), align.count('s')]
    wscore = [-2, -2, 3, -1]
    align_score = np.dot(align_count, wscore)
    
    print "Native: ", native
    print "Align: ", align
    
    hom1 = make_hom(native, align)
    hom = [3,2,1,2,5,5,3,2,1,4,7,6,5,2]  
    print "Homolg0", hom
    print "Homolg1", hom1
    #print lst2str(native)
    #print lst2str(hom)
    
    num_decoys = 10
    decoys = []
    decoy_seq_len = len(native)
    
    for i in range(num_decoys):
        decoys.append(make_sequence(pool,decoy_seq_len))
    #print "Decoys: ", len(decoys)
    
    print "Align score: ", align_score, align_count, wscore
    aligns(lst2str(native), lst2str(hom))

def test3():
    native = make_native(10)
    print "Native:  ", native
    align = make_alignment_list(6)
    print "Align:   ", align
    #sub = make_sublist(native,align)
    sub = make_sub(native, len(align))
    print "Sub:     ", sub
    hom = make_hom(align, sub)
    print "Hom:     ", hom
    hom = pad(hom, pool)
    print "Homolog: ", hom
    
    align_count = [align.count('d'), align.count('i'), align.count('m'), align.count('s')]
    wscore = [-2, -2, 3, -1]
    align_score = np.dot(align_count, wscore)
    
    
    
    
    

    num_decoys = 10
    decoys = []
    dseq_len = len(native)
    
    for i in range(num_decoys):
        decoys.append(make_sequence(pool,dseq_len))
    #print "Decoys: ", len(decoys)
    
    #print lst2str(native), lst2str(hom)
    print "Align score: ", align_score
    aligns(lst2str(native), lst2str(hom))
    
def main():          
    global pool, native
    pool = make_pool()
    test1()
    
    
    


if __name__ == '__main__':
    main()
    #plot(native)
