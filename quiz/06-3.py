def getTotalPage(m,n):
    if m % 10 ==0:
        return m//n
    else:
        return m//n +1

print(getTotalPage(25,10))