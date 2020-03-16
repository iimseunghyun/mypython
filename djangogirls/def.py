s = "python is the best choice"

def findword(a):
    f = s.find(a)
    l = len(a)
    print(s[f:f+l])

    if f == -1:
        print(a+"검색: \"%s\"는 없는 문자입니다." %a)
    else :
        print(a+"는 %d번째 문자입니다." %f)    



findword("is")
findword("me")