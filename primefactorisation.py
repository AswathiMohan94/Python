num=input("enter the integer : ")
p=[]

for i in range(2,(num/2)+1,1):
	mid=(i/2)
	count=0
	if i in (0,1):
		continue
	for j in range(2,mid+1,1):
		if(i%j)==0:
			count=count+1
	if count==0:
		p.append(i)

while num!=1:
	i=0
	r=1
	while r!=0:
		x=p[i]
		if((num%x)==0):
			num=num/x
			r=0
			print(x)
		else:
			i=i+1
			
			
					
