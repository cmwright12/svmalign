from Bio import pairwise2
from Bio.pairwise2 import format_alignment
from Bio.pairwise2 import dictionary_match
from makedataset_letters import aligns

match_score = 1
mismatch_score = 0
substitution_score = 0
gap_score = -1

score_dict = {
('a','b'): substitution_score,
('b','c'): substitution_score,
('c','d'): substitution_score,
('d','e'): substitution_score,
('e','f'): substitution_score,
('f','g'): substitution_score,
('g','h'): substitution_score,
('h','i'): substitution_score,
('i','j'): substitution_score,
('j','k'): substitution_score,
('k','l'): substitution_score,
('l','m'): substitution_score,
('m','n'): substitution_score,
('n','o'): substitution_score,
('o','p'): substitution_score,
('p','q'): substitution_score,
('q','r'): substitution_score,
('r','s'): substitution_score,
('s','t'): substitution_score,
('t','a'): substitution_score
}

for letter in list('abcdefghijklmnopqrst'):
    score_dict[(letter,letter)] = match_score

MatchDict = dictionary_match(score_dict, symmetric=0)

s1 = 'aggtabrgct--g'
s2 = 'afhadbrgrlmac'
align_dict = {'m': 0, 's': 0, 'i': 0, 'd': 0}

def matching(s1,s2):
    sum = 0
    for i in range(len(s1)):
        if s1[i] == '-' or s2[i] == '-':
            print gap_score,
            sum += gap_score
            if s1[i] == '-':
                align_dict['i'] += 1
            else:
                align_dict['d'] += 1
        else:
            if (s1[i],s2[i]) in score_dict:
                sub = MatchDict.__call__(s1[i],s2[i])
                print sub,
                sum += sub
                if s1[i] == s2[i]:
                    align_dict['m'] += 1
                else:
                    align_dict['s'] += 1
            else:
                print mismatch_score,
                sum += mismatch_score
    print
    print align_dict
    return sum
print s1
print s2
print "Score: ", matching(s1,s2)

align_dict = {'m': 0, 's': 0, 'i': 0, 'd': 0}
def matching2(s1,s2):
    sum = 0
    for i in range(len(s1)):
        if (s1[i],s2[i]) in score_dict:
            sub = MatchDict.__call__(s1[i],s2[i])
            sum += sub
            if s1[i] == s2[i]:
                align_dict['m'] += 1
            else:
                align_dict['s'] += 1
        elif s1[i] == '-' or s2[i] == '-':
            sum += gap_score
            if s1[i] == '-':
                align_dict['i'] += 1
            else:
                align_dict['d'] += 1
        else:
            sum += mismatch_score
    return sum
    
print
print s1
print s2
print "Score: ", matching2(s1,s2)
print align_dict
print aligns(s1,s2)


