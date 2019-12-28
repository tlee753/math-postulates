import sys
import random

def count_elements(seq) -> dict:
    """Tally elements from `seq`."""
    hist = {}
    for i in seq:
        hist[i] = hist.get(i, 0) + 1
    return hist

def ascii_histogram(seq) -> None:
    """A horizontal frequency-table/histogram plot."""
    counted = count_elements(seq)
    for k in sorted(counted):
        print('{0:5d} {1}'.format(k, '+' * counted[k]))

def zipf(n=100,r=10):
    l = list(range(n))
    for _ in range(r):
        while True:
            rand1 = random.randint(0, n-1)
            rand2 = random.randint(0, n-1)
            if (rand1 != rand2):
                break            
        x = l[rand1] 
        y = l[rand2] 
        if x < y:
            l[rand2] = x
        else:
            l[rand1] = y
        
#    print(l)
#    print()
#    l.sort()
#    print(l)
    ascii_histogram(l)

zipf(int(sys.argv[1]), int(sys.argv[2])) 
