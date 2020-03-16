def quickSort(a):
    l = len(a)     
    if l <= 1:
        return a
        
    pi = a[0]
    pivot = [pi]
    left = []
    right = []

    for idx in range(1,len(a)):
        if a[idx] > pi:
            right.append(a[idx])
        elif a[idx] <= pi:
            left.append(a[idx])
    
    return quickSort(left) + pivot + quickSort(right)
 

a = [5, 9, 2, 4, 1, 7, 10, 3, 8, 11, 6]
print(quickSort(a))

