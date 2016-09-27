import makedataset_letters
import numpy as np
import random

"""
w
f
D
"""

match = 3
mismatch = -1
gap = -2

# define cost vector [match, mismatch, gap]
w = np.asarray([match, mismatch, gap])

def make_align(s1,s2, match=1, mismatch=0, gap=-1):
    align = ''
    for i in range(len(s1)):
        if s1[i] == s2[i]:
            align += 'm'
        elif s1[i] == '-' or s2[i] == '-':
            align += random.choice(['d','i'])
    return align


def fa(s1,s2,align):
    num_matches = align.count('m')
    num_mismatches = align.count('s')
    num_gaps = align.count('i') + align.count('d')
    features = np.asarray([num_matches, num_mismatches, num_gaps])
    return features

def f(s1,s2):
    align = make_align(s1,s2)
    num_matches = align.count('m')
    num_mismatches = align.count('s')
    num_gaps = align.count('i') + align.count('d')
    features = np.asarray([num_matches, num_mismatches, num_gaps])
    return features
    
def Da(s1,s2,align):
    return np.dot(w, f(s1,s2,align))
    
def D(s1,s2):
    max = 0
    for a in alignments:
        if Da(s1,s2,a) > max:
            max = Da(s1,s2,a)
    return max