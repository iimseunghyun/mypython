def input2List():
    # 1 1, 2 2, a a
    # newList = [3(0),7(1),9]
    newList = []

    while True:
        a = input()
        idx = 0
        if a == 'x':
            break
        # newList.append(a)
        # n = len(newList)
        # if n <= 0:
        #     newList.append(a)
        # for i in range(n):
        #     if newList[i] > a:
        #         newList.insert(i,a)
        #         break
        #     if i == n-1:
        #         newList.append(a)
        start = 0
        end = len(newList) - 1
        while start <= end:
            # mid = len(newList) // 2
            mid = (start + end) // 2
            if a == newList[mid]:
                # 값이 같으면
                # newList.insert(mid,a)
                idx = mid
                break
            elif a > newList[mid]:
                # 입력값이 작으면
                start = mid +1
                # start >= end
                if start >= end:
                    idx = mid + 1
                    # break
            # elif a < newList[mid]:
            else:
                # 입력값이 크면
                end = mid -1
                # start >= end
                if start >= end:
                    idx = mid
                    # break
        
        newList.insert(idx,a)

    return newList

if __name__=='__main__':
    result = input2List()
    print(result)