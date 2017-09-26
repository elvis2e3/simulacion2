l=[0.0449,0.6015,0.6300,0.5514,0.0207,
	0.1733,0.6694,0.2531,0.0316,0.1067,
	0.5746,0.3972,0.8297,0.3587,0.3588,
	0.0490,0.7025,0.6483,0.7041,0.1746,
	0.8406,0.1055,0.6972,0.5915,0.3362,
	0.8349,0.1247,0.9582,0.2523,0.1585,
	0.9200,0.1977,0.9085,0.2545,0.3727,
	0.2569,0.0125,0.8524,0.3044,0.4145]

n=40
m=5
fe=n/float(m)
pm=1/float(m)
saltos=[]
x=0
while x<=1:
	saltos.append(x) 
	x+=pm
print saltos
lista=[0]*m
#print lista
for i in l:
	for j in range(m):
		if saltos[j] <= i <= saltos[j+1]:
			lista[j]+=1 
print lista
X2=1/float(fe)
m=0
for i in lista:
	m=m+pow(i-fe,2)
X2=X2*m
print X2
