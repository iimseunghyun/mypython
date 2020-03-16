# number = input('숫자를 입력하세요 ')
# print(number)


# def choolgyul(classday):
classday= input('이번 달 소정일수를 입력하세요:')
classday= int(classday[0])
x = input('''출결현황을 "결석/지각/조퇴/외출"의 형태로 따옴표 없이 입력하세요:''')
a = []
a = x.split('/')
b = int(a[3])+int(a[1])+int(a[2])
c = b // 3 + int(a[0])
print("총 출석차감일수: %d" %c)
if (classday-c)>=20:
    print('수당100%')
elif (classday-c)<(classday*0.8):
    print ('수당zero')
else:
    print('수당차감')

# choolgyul(21)