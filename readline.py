# for i in range(1,10):
#     for j in range(2,5):
#         print("%dx%d = %d"%(j,i,i*j), end= '  ' )
#     print('')

# for i in range(1,10):
#     for a in range(5,8):
#         print ("%dx%d = %d"%(a,i,i*a), end= '  ' )
#     print('')    

# for i in range(1,10):
#     for a in range(8,10):
#         print ("%dx%d = %d"%(a,i,i*a), end= '  ' )
#     print('')    

data1 = ""
f=open("gugudan.txt", 'w')

for i in range(1,10):

    for j in range(2,5):
        data1 = data1 + "%dx%d = %d "%(j,i,i*j) 
    data1 +='\n'
    
for i in range(1,10):

    for j in range(5,8):
        data1 = data1 + "%dx%d = %d  "%(j,i,i*j)
    data1 += '\n'

for i in range(1,10):

    for j in range(8,10):
        data1 += "%dx%d = %d  "%(j,i,i*j)
    data1 += '\n'





f.write(data1)

f.close()
