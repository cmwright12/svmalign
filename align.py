from Bio import pairwise2
from Bio.pairwise2 import format_alignment
"""
The names of the alignment functions in this module follow the convention <alignment type>XX where <alignment type> is either "global" or "local" and XX is a 2 character code indicating the parameters it takes. The first character indicates the parameters for matches (and mismatches), and the second indicates the parameters for gap penalties.

The match parameters are:
CODE  DESCRIPTION
x     No parameters.  Identical characters have score of 1, otherwise 0.
m     A match score is the score of identical chars, otherwise mismatch score.
d     A dictionary returns the score of any pair of characters.
c     A callback function returns scores.

The gap penalty parameters are:

CODE  DESCRIPTION
x     No gap penalties.
s     Same open and extend gap penalties for both sequences.
d     The sequences have different open and extend gap penalties.
c     A callback function returns the gap penalties.
"""

#print("local: match = 1, mismatch = 0, gap = 0")
#for a in pairwise2.align.localxx("ACCGT", "ACG"):
#    print(format_alignment(*a))

print("local: match = 3, mismatch = 0, gap = -2")
for a in pairwise2.align.localms("5292135521921", "32125532147652",3,-2):
    print(format_alignment(*a))