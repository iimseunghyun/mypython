a = [71, 49, 33, 21, 86, 93]
x = a[0]
for idx in range(1,len(a)):
    if x >= a[idx]:
        x=a[idx]
        minidx = idx

print(minidx)

