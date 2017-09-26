Z0=1009
r=1
n=1
while r!=0:
	n8=pow(Z0,2)
	Z2=str(n8)
	if len(Z2)<8:
		x=8-len(Z2)
		Z2=("0"*x)+Z2
	Z1=Z2[2:6]
	r=float("0."+Z1)
	print n,Z0,Z2,r
	Z0=int(Z1)
	n+=1
