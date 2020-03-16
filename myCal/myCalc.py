from calcUtil import CalcExp

def runCalc():
    while True:
        inputStr = input()
        calcExp = CalcExp(inputStr)
        calcExp.rmSpace()
        if calcExp.exp == "x":
            return
        calcExp.rmChars()
        expLst = calcExp.exp2lst()
        print(expLst)

runCalc()
