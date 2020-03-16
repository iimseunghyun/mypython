
#입력
start = input("숫자와 연산자 띄어쓰기하여 입력:")

#입력 된 값을 리스트화
question= start.split()
l = len(question)

operators= []
numbers= []
for index in range(l):
    #연산자
    if index %2 == 1:
        operators.append(question[index])
       
    #숫자
    else:
        numbers.append(int(question[index]))    

print(operators, numbers)    


while question :
    if '*' in question:
        muIdx = question.index('*')
        result1=int(question[muIdx-1]) * int(question[muIdx+1])
        del question[muIdx-1:muIdx+2] 
        question.insert(muIdx-1,result1)

    if '/' in question:
        diIdx = question.index('/')
        result2=int(question[diIdx-1]) / int(question[diIdx+1])
        del question[diIdx-1:diIdx+2]
        question.insert(diIdx-1,result2)

    if '+' in question:
        plIdx = question.index('+')
        result3=int(question[plIdx-1]) + int(question[plIdx+1])
        del question[plIdx-1:plIdx+2]
        question.insert(plIdx-1,result3)

    if '-' in question:
        miIdx = question.index('-')
        result4=int(question[miIdx-1]) - int(question[miIdx+1])
        del question[miIdx-1:miIdx+2]
        question.insert(miIdx-1,result4)
    
    if l == 1:
        break
    
    print(question)
