src = [5,4,1,2,3]
trg = []

tmp = src.pop(0)
trg.append(tmp)



tmp = src.pop(0)
if tmp <trg[0]:
    trg.insert(0,tmp)
else:
    trg.insert(1,tmp)



minIdx=0
tmp = src.pop(0)
for idx in range(len(trg)):
    if tmp < trg[idx]:
        if trg[idx] <=trg[minIdx]:
                minIdx = idx
    else:
        minIdx = idx+1
trg.insert(minIdx,tmp)



minIdx=0
tmp = src.pop(0)
for idx in range(len(trg)):
    if tmp < trg[idx]:
        if idx <=minIdx:
                minIdx = idx
    else:
        minIdx = idx+1
trg.insert(minIdx,tmp)



minIdx=0
tmp = src.pop(0)
for idx in range(len(trg)):
    if tmp < trg[idx]:
        if idx<=minIdx:
                minIdx = idx
    else:
        minIdx = idx+1
trg.insert(minIdx,tmp)

print(trg)