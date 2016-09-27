from Bio import pairwise2
from Bio.pairwise2 import format_alignment
from Bio.pairwise2 import dictionary_match
from makedataset_letters import aligns

match_score = 2
mismatch_score = -1
substitution_score = 0
gap_score = 0

LETTERS = list('abcdefghijklmnopqrst')
score_dict = {}

for i in range(len(LETTERS)):
    score_dict[(LETTERS[i], LETTERS[i])] = match_score
    score_dict[(LETTERS[i], LETTERS[(i+1)%20])] = substitution_score

MatchDict = dictionary_match(score_dict, symmetric=0)

#s1 = 'aggtabrgct--g'
#s2 = 'afhadbrgrlmac'

s1='accgt'
s2='a-cg-'

align_dict = {'m': 0, 's': 0, 'i': 0, 'd': 0}

 
def compare(a,b):
    if (a,b) in score_dict:
        if a==b:
            align_dict['m']+=1
        else:
            align_dict['s']+=1  
        return MatchDict(a,b)
    elif a == '-' or b == '-':
        if a=='-':
            align_dict['d']+=1
        else:
            align_dict['i']+=1
        return gap_score
    else:
        return mismatch_score

def score(d):
    return match_score*d['m'] + substitution_score*d['s'] + gap_score*(d['i']+d['d'])
        
print map(compare, s1, s2)
print align_dict
print s1
print s2
print "Score: ", score(align_dict)
print "-----biopython-----"
print aligns('accgt','acg')
print aligns('accgt','ac-g-')
