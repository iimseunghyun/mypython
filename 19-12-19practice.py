# def multi(a):
#     result=1
#     for n in range(1,a+1):
#         result = result * n
#     return result


# print (multi(10))


#재귀함수
def fact(n):
    if n <= 1:                  #출구
        return 1
    return n*fact(n-1)

print(fact(10))