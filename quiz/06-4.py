import sys


# if sys.argv[1] == 'w':
#     f = open("new.txt",'w')
#     f.write("%s\n" %sys.argv[2])
#     f.close()
#     f= open("new.txt",'r')
#     print(f.read())
#     f.close()
if sys.argv[1] == 'a':
    f = open("new.txt",'a')
    f.write("%s\n" %sys.argv[2])
    f.close()
    f= open("new.txt",'r')
    print(f.read())
    f.close()

elif sys.argv[1] == 'r':
    f = open("new.txt", 'r')
    print(f.read())
    f.close()

