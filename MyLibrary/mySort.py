class MySort:
"""
선택,삽입,병합,퀵,거품 정렬 알고리즘
"""

    def bubble(self, a):
        """
        버블정렬
        """
        l = []
        for i in a:
            x = 0
            if len(l) == 0:
                l.append(i)
            else:
                for j in l:
                    if i > j:
                        x += 1
                    elif i < j:
                            l.insert(x,i)
                            break            
        return (l)

    def quickSort(a):
        """
        퀵정렬
        """
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