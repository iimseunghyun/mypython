n3 = "33333....333333....333333"

for x in range(5):
    n=[]
    for y in range(5):
        n.append(n3[x*5+y])
    print("%s%s%s%s%s" %(n[0],n[1],n[2],n[3],n[4]))