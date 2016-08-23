### added on branch?
### construction of synthetic dataset
###

import random
import matplotlib.pyplot as plt
import numpy as np
#import seqfunctions

num_natives = 1
alldecoys = set([])

# 20 letter alphabet S=1..20 where each c in S has c/210 probability of being drawn
pool = make_pool()

for n in range(num_natives):
# make native sequence and decoys of length 50, 10 decoys per native
    nseq_length = 10
    aseq_length = 6
    native = make_native(nseq_length)
    align = make_alignment_list(aseq_length)

    align_count = [align.count('d'), align.count('i'), align.count('m'), align.count('s')]
    # d, i, m, s
    wscore = [-2, -2, 3, -1]
    align_score = np.dot(align_count, wscore)
    
    print "Native: ", native
    print "Align: ", align

    # GENERATING THE HOMOLOG
    # 1 generate alignment string of length 30 using 'msid'
    # 2 apply alignment string to randomly selected substring of the native
    # 3 pad shortened sequences with additional random characters 
    hom = make_hom(native, align)
    hom = pad(hom, pool)
  
    print "Homolog", hom

    num_decoys = 10
    decoys = []
    dseq_len = len(native)
    
    for i in range(num_decoys):
        decoys.append(make_sequence(pool,dseq_len))
    #union to set alldecoys
    
    # breakdown alignment score from biopython
    print "Align score: ", align_score
    aligns(lst2str(native), lst2str(hom))





