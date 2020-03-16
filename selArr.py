d = [2,4,5,1,3]  
#각각의 변수로 대입하는 것보다 리스트로 묶어주면 변수,값에 순서까지 갖게 된다.

def find_minIdx(lst):
    minIdx=0
    n=len(d)
    for i in range(1,n):
        if d[minIdx] > d[i]:
            minIdx=i
            print(minIdx)
    return minIdx

def sel_Arr(d):
    result = []
    while d:
        minIdx = find_minIdx(d)
        value = d.pop(minIdx)
        result.append(value)
    return result

print(sel_Arr(d))