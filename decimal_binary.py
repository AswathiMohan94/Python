
def swap(x):
	
	return((x & 0x0F)<< 4|(x & 0xF0)>>4)

a=input("enter the integer : ")
c=bin(a)
print ("the binary value of the entered integer is :",c)
b=swap(a)
d=bin(b)
print("the binary value after swapping the new integer is : ",d)
print (" decimal value of the new integer is : ",b)



