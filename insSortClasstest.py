class InsSort: #사용자 자료형
    def __init__(self,src):
        self.src= src        
    def Fn(self):
        trg=[]
        while self.src:
            tmpIdx = 0
            tmp = self.src.pop(0)
            for index in range(len(trg)):
                if tmp < trg[index]:
                    if index ==0:
                        pass
                    else: 
                        if trg[index]<trg[tmpIdx]:
                            tmpIdx = index
                else:
                    tmpIdx = index+1
            trg.insert(tmpIdx,tmp)
        return trg

a = InsSort([5,4,1,2,3])
print(a.Fn())