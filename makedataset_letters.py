import random
import numpy as np
from Bio import pairwise2
from Bio.pairwise2 import format_alignment

# http://www.codeskulptor.org/#user41_uQt9Z1txPs_0.py

alphabet = list("abcdefghijklmnopqrst")
len_N = 20
len_A = int(2 * len_N / 3)


def make_pool():
    """Uses 20 letters a-t to make list of 210 letters [a,b,b,c,c,c,d,d,d,d,...]"""
    pool = []
    
    for letter in alphabet:
        for count in range(alphabet.index(letter)+1):       
            pool.append(letter)
    return pool

pool = make_pool()
    
def make_native_sequence(pool):
    """Make a sequence of length len_N using the pool"""
    native = ''
    for i in range(len_N):
        native += random.choice(pool)
    return native
 
def make_alignment_string(alength=len_A):
    """Make an alignment string of length len_A"""
    align_pool = 'm'*4 + 's'*2 + 'i'*2 + 'd'*2
    align_pool_list = list(align_pool)
    alignment = ''
    for i in range(alength):
        alignment += random.choice(align_pool_list)
    align_count = {'d': alignment.count('d'), 'i': alignment.count('i'), 'm': alignment.count('m'), 's': alignment.count('s')}
    return alignment, align_count

def make_substring(native):
    diff = len_N - len_A
    start = random.randrange(0, diff)
    if len_A < diff:
        length = random.randrange(len_A, diff)
    else:
        length = random.randrange(diff, len_A)
    stop = start + length
    
    sublist = native[start:stop]
    begin = native[0:start]
    end = native[stop:len_N]
    return sublist, begin, end
    
    
def apply_alignment(aln, sub):
    sub = list(sub)

    index = 0
    hom = sub[:]
    for a in aln:
        #print "Sublist: ", sub, ", a: ", a, ", Index: ", index
        #print "Sub_len: ", len(sub)
        if a == 's':
            ix = alphabet.index(sub[index])
            hom[index] = alphabet[(ix - 1) % 20]
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
            #print 'd', index
            del hom[index]
    

    return hom
    
def make_hom(natv):
    sub, begin, end = make_substring(natv)
    hom = sub[:]
    print "Sub:       ", sub
    aln, aln_count = make_alignment_string(len(sub))
    print "Alignment: ", aln
    hom = apply_alignment(aln, sub)
    return begin + ''.join(hom) + end
    #return ''.join(hom)
    
def aligns(s1,s2):
    print("local: match = 3, mismatch = -1, gap = -2")
    for a in pairwise2.align.localms(s1,s2,3,-1,-2,-2):
        print(format_alignment(*a))

    
def test():
    
    native = make_native_sequence(pool)
    print "Native:    ", native

    hom = make_hom(native)
    

    print "Homolog:   ", hom
    
    # GENERATING THE HOMOLOG
    # 1 generate alignment string of length 30 using 'msid'
    # 2 apply alignment string to randomly selected substring of the native
    # 3 pad shortened sequences with additional random characters 
    
    aligns(native,hom)
    

def make_decoy(len_D, native):
    pass
    
    
def main(): 
    
    test()
    
    
    


if __name__ == '__main__':
    main()