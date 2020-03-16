# string to dictionary
# str[0]는 key, 나머지는 value
def str2dic(str) :
    dic = {str[0]:[]}
    tmp = []
    for i in range(1, len(str), 1) :
        tmp.append(str[i])
    dic[str[0]] = tmp
    return dic
