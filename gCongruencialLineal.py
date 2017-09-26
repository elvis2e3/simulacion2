n=0
a=5
c=7
X0=7
m=8
limite=20
while n<limite:
	modulo=(a*X0+c)%m
	X1=modulo/float(m)
	print n,X0,modulo,X1
	X0=modulo
	n+=1

