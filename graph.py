soc = {
    'A': ['B','C','E'],
    'B': ['A','C','F'],
    'C': ['A','B','D','F'],
    'D': ['C','E'],
    'E': ['A','D','F'],
    'F': ['B','C','E','G'],
    'G': ['F'],
    'H': ['I'],
    'I': ['H']
}
#2촌
def graph(p):
    lst = []
    for i in soc[p]:
        lst += soc[i]
    s = set(lst)
    lst2 = list(s)
    lst2.remove(p)
    for j in soc[p]:
        if j not in lst2:
            continue
        lst2.remove(j)
    
    return lst2


a= input("KEY:")
print(graph(a))