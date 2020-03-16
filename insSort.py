src = [5,4,1,2,3]
trg = []

tmp = src.pop(0)
trg.insert(0,tmp)

tmp = src.pop(0)
if tmp>trg[0]:
    trg.append(tmp)
trg.insert(0,tmp)




print(trg)