import sys 

src = sys.argv[1]
dst = sys.argv[2]

f = open(src, 'r')
tmp = f.read()
print(tmp)
f.close()

space =tmp.replace("\t"," "*4)

f =open(dst, 'w')
f.write(space)
f.close()