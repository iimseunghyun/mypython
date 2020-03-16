def sum(n):
    a = 0
    for i in range(1,n+1):
        a = a + i
        print("a는 %d, i는 %d" %(a,i))
    return a

s = sum(5)
print(s)