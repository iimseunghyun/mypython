def find_friends(dic,start):
    qu = []
    path = {}
    done = set()
    qu.append(start)
    while qu:
        qu_item = qu.pop(0)
        x = qu_item[-1]
        done.add(x)
        for item in dic[x]:
            if item not in done:
                qu.append(qu_item + item)
                if item not in path:
                    path[item] = len(qu_item)
                elif path[item] > len(qu_item):
                    path[item] = len(qu_item)
                else:
                    pass                                       
    return path

if  __name__ == '__main__':
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

print(find_friends(soc,'A'))