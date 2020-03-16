#동명이인 이름 찾기

lst=['tom', 'jerry', 'ben', 'tom','ben']
n=list()
for name in lst:
    #n=list()가 이 위치에 있는 경우, 최근 a>1인 요소만 들어가게됨.
    a= lst.count(name)
    if a>1:
        #n=list()가 이 위치에 있는 경우, 최근 a>1인 요소만 들어가게됨.
        n.append(name)
        
print(list(set(n)))


newLst = []
# for i in range(len(lst)-1):
#     for j in range(i+1,len(lst)):
#         source = lst[i]
#         target = lst[j]
#         bl = source == target
#         if bl:
#             newLst.append(source)
#         print('%d(%s):%d(%s),%s' %(i,source,j,target,bl))
# print('same name =%s' %newLst)

for i in range(len(lst)-1):
    for j in range(i+1,len(lst)):
        source=lst[i]
        target=lst[j]
        bl = source == target
        if bl:
            newLst.append(source)
print(newLst)


for item in lst:
    
    lst2.append(item)



alp=['a', 'b', 'b', 'a', 'c']
