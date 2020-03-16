# from bigCal import BigNum


class FourCal:
#생성자 메서드
    def __init__(self,first,second):             
        self.first = first
        self.second = second

#메서드
    def setdata(self, first, second): 
        self.first = first
        self.second = second
    
    def add(self):
        result = self.first + self.second
        return result
    
    def sub(self):
        result = self.first - self.second
        return result

    def mul(self):
        result = self.first * self.second
        return result
    
    def div(self):
        result = self.first / self.second
        return result


if __name__ == "__main__":
    #먼저 객체를 생성하고
    myCal = FourCal(5,5)

    #메서드를 사용한다.
    myCal.setdata(4,2)
    print(myCal.first, myCal.second)
    print(myCal.add())
    print(myCal.sub())
    print() 