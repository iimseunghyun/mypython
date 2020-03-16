from str2dic_tool import *

'''
│ ┌─────┐
│a│b c d│
│ │  ───│
│e│f g h│
│ │ ┌─┐ │
│i│j│k│l│
│m n o│p│
└─────┘ │
'''
# create dictionary
# a 에서 갈수 있는 위치 e 를 키값으로 갖는다
# str2dic('ae') >> 'a':['e'] ...
# dic1.update(dic2) 는 dic1에 dic2를 update한다
# dictionary.txt 내용처럼 만든다.
dic = str2dic('ae')
dic.update(str2dic('bfc'))
dic.update(str2dic('cbd'))
dic.update(str2dic('dc'))
dic.update(str2dic('eai'))
dic.update(str2dic('fbgj'))
dic.update(str2dic('gfh'))
dic.update(str2dic('hgl'))
dic.update(str2dic('iem'))
dic.update(str2dic('jfn'))
dic.update(str2dic('ko'))
dic.update(str2dic('lhp'))
dic.update(str2dic('min'))
dic.update(str2dic('njmo'))
dic.update(str2dic('okn'))
dic.update(str2dic('pl'))

'''
now : 현재위치 
next: 다음위치
next에 다음에 갈수 있는 위치를 저장
now의 next경로와 next에서 now로 돌아가는 경로를 지운다
next로 갈 위치가 없으면 path에서 now를 제거하고 
path의 마지막에서 다시 시작한다
'''
# init
path = ['a']
now = 'a'
next = None

while now != 'p' :          # p에 도착하면 종료
    if len(dic[now]) == 0 : # 경로가 더이상 없으면
        path.pop()          # now를 path에서 제거후
        now = path[-1]      # 마지막 부분으로 now를 변경한다
    else :
        next = dic[now][0]              # next
        del dic[now][0]                 # now의 next경로삭제
        for i in range(len(dic[next])) :# next의 now경로삭제(거꾸로 돌아오는 경로)
            if dic[next][i] == now :    
                del dic[next][i]
                break
        now = next          # 이동
        path.append(now)    # now를 path에 추가

print(path)