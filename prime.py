a=input("enter the lower limit : ")
b=input("enter the upper limit : " )
print "the prime nos in the given range are : "
for num in range(a,b+1):
	if num>1:
		for i in range(2,num):
			if(num%i)==0:
				break
		else:
			print(num)
