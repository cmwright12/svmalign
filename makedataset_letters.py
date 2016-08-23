import random
import numpy as np

def make_pool():
    """Uses 20 letters a-t to make list of 210 letters [a,b,b,c,c,c,d,d,d,d,...]"""
    alphabet = list("abcdefghijklmnopqrst")
    pool = []
    
    for letter in alphabet:
        for count in range(alphabet.index(letter)+1):       
            pool.append(letter)
    return pool
    
def make_native_sequence(len_N, pool):
    """Make a sequence of length len_N using the pool"""
    native = ''
    for i in range(len_N):
        native += random.choice(pool)
    return native
 
def make_alignment_string(len_A):
    align_pool = 'm'*4 + 's'*2 + 'i'*2 + 'd'*2
    alignment = ''
    for i in range(len_A):
        alignment += random.choice(list(align_pool))
    return alignment

def make_substring(native, min_len):
    
    
    
def apply_alignment(alignment, native):
    #substring = make_substring(native, len(alignment))
    #return substring
    
def test():
    len_N = 20
    len_A = int(2 * len_N / 3)

    pool = make_pool()
    native = make_native_sequence(len_N, pool)
    alignment = make_alignment_string(len_A)
    
    print native
    print alignment
    
    # GENERATING THE HOMOLOG
    # 1 generate alignment string of length 30 using 'msid'
    # 2 apply alignment string to randomly selected substring of the native
    # 3 pad shortened sequences with additional random characters 
    
    

def make_decoy(len_D, native):
    pass
    
    
def main():          
    test()
    
    
    


if __name__ == '__main__':
    main()