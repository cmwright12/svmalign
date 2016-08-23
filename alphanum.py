
# convert string a-t to list 1-20
def str2lst(mystring):
    alpha = list('abcdefghijklmnopqrst')
    nums = range(1,21)
    d = dict(zip(alpha,nums))
    mylist = [d[letter] for letter in mystring]
    return mylist


# convert list 1-20 to string a-t
def lst2str(mylist):
    alpha = list('abcdefghijklmnopqrst')
    mystring = [alpha[num-1] for num in mylist]
    mystring = ''.join(mystring)
    return mystring

def main():
    phrase = 'ajcrssaibcc'
    print phrase
    a = str2lst(phrase)
    print "Convert: ", a
    b = lst2str(a)
    print "Convert: ", b
    print "Same? ", phrase == b
    hom = [3,2,1,2,5,5,3,2,1,4,7,6,5,2]
    print lst2str(hom)
    
if __name__ == '__main__':
    main()