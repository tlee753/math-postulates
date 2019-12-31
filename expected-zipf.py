import sys

n = int(sys.argv[1])
values = []
for i in range(1,n+1):
    values.append(round(n*(1/i), 2))

print(values)