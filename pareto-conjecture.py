import sys


def pareto(n):
    n = int(n)
    sum20 = 0.0
    sum80 = 0.0
    for i in range(1, n+1):
        if i < n*0.2:
            sum20 += 1.0/i
        else:
            sum80 += 1.0/i  
    total = sum20 + sum80
    print("Sum 20: {:0.3f}  {:0.3f}%".format(sum20, sum20/total))
    print("Sum 80: {:0.3f}  {:0.3f}%".format(sum80, sum80/total))
    print("Total: %f" % total)

pareto(sys.argv[1])


### Notes
# anything between ~400 and 30000 is within 5% of the 80-20 rule
# anything between ~120 and 10000000 is within 10% of the 80-20 rule
# ~1800 is about exactly 80-20 split
