src = [5,4,1,2,3]

# tmp = src.pop(0)
# trg.append(tmp)



# def myFn1(pa):
#     tmp = pa.pop(0)
#     tmplst= trg[:]
#     if tmp < tmplst[0]:
#         tmplst.insert(0,tmp)
#     else:
#         tmplst.insert(1,tmp)
#     return tmplst

# trg = myFn1(src)
# print(trg)



# def myFn2():
#     tmp = src.pop(0)
#     tmplst= trg[:]
#     if tmp < tmplst[0]:
#         tmplst.insert(0,tmp)
#     else:
#         tmplst.insert(1,tmp)
#     return tmplst

# trg = myFn2()
# print(trg)



# def myFn3(pa):
#     tmp = pa.pop(0)
#     if tmp < trg[0]:
#         trg.insert(0,tmp)
#     else:
#         trg.insert(1,tmp)

# myFn3(src)
# print(trg)



# def myFn4():
#     tmp = src.pop(0)
#     if tmp < trg[0]:
#         trg.insert(0,tmp)
#     else:
#         trg.insert(1,tmp)

# myFn4()
# print(trg)



def myFn5(pa):
    trg=[]
    while pa:
        tmpIdx = 0
        tmp = pa.pop(0)
        for index in range(len(trg)):
            if tmp < trg[index]:
                if index ==0:
                    pass
                else: #1,2,3
                    if trg[index]<trg[tmpIdx]:
                        tmpIdx = index
            else:
                tmpIdx = index+1
        trg.insert(tmpIdx,tmp)
    return trg


print(myFn5(src))