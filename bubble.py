
def bubble(a):
    l = []
    for i in a:
        x = 0
        if len(l)==0:
            l.append(i)
        else:
            for j in l:
                if i > j:
                    x += 1
                elif i < j:                
                    break            
            l.insert(x,i)        
    return (l)



# if __name__ == "__main__"
lst = [6,7,8,2,4,1,3,10,5]
print(bubble(lst))