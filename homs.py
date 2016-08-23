import random

alphabet = range(1,21)
native = [15, 13, 15, 20, 18, 8, 9, 17, 19, 20]
align = ['d', 's', 'd', 'i', 'i', 'm']


hom = native
print native
print align
print


def make_substring():
    for i in range(5):
        start = random.randrange(0,6)
        length = random.randrange(4,)
        sub = native[start:start+length]

def make_hom(native, align):
    for index in range(align):
        c = align[index]
        if c == 's':
            hom[index] = (c % 20) + 1

