

class Ball:
    num=7

    def changeNum(self,p):
        self.num = p

a=Ball()  # 클래스 실행
a.num =9
print(a.num)

a.changeNum(1)
print(a.num)

class RedBall(Ball):
        color = 'red'

b = RedBall()
print(b.num)


    
