class MySort2:
    def __init__(self):
        self.lst = []
        

    def myinput(self):
        self.a= input("자연수 하나씩 입력(종료는 x입력):")
        return self.a
        
    def sorting(self):
        self.num = int(self.a)
        l = len(self.lst)
        x = 0
        if l == 0:
            self.lst.append(self.num)
        else:
            for i in self.lst:
                if self.num <= i:
                    break
                elif self.num > i :
                    x += 1
            self.lst.insert(x, self.num)
            
        return print(self.lst)

    def rep(self):
        while True:
            if self.myinput() == 'x':
                break
            self.sorting()



q = MySort2()
q.rep()