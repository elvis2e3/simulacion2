n=0
a=17
X0=51
m=37
limite=20
while n<limite:
	modulo=(a*X0)%m
	X1=modulo/float(m)
	print n,X0,modulo,X1
	X0=modulo
	n+=1

