temp=[]
rn=[]
def sorting(n):
    minN= n[0]
    for idx in range(1,len(n)):
        if n[idx]<minN:
            minN=n[idx]
        

    temp.append(minN)
    n.remove(minN)
    # rn=n[:]
    return n #rn 
    
    # return temp


print(sorting(sorting([5,3,1,2,4])))
# sorting(sorting(sorting([5,3,1,2,4])))

print (temp)


#2. 임시리스트에 담기
    # temp.append(minn)
    # n.remove(minn)





