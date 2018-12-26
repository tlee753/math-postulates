total = 0.0
for i in range(1, 76):
    total += 1.0/i

print(total)

subtotal = 0.0
for i in range(1, 76):
    subtotal += 1.0/i
    if ((subtotal/total) > 0.5):
        print(subtotal)
        print(i)
        break
