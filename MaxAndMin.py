n=int(input("enter the limit : "))
arr=[]
print("enter the nos in the array : ")
for i in range(0,n,1):
	x=int(input())
	arr.append(x)
	
max1=arr[0]
min1=arr[0]
for i in range(0,n,1):
	if arr[i]>max1:
		max1=arr[i]
	if arr[i]<min1:
		min1=arr[i]
min2=max1
max2=min1
for i in range(0,n,1):
	if arr[i]>max2 and arr[i]<max1:
		max2=arr[i]
	if arr[i]<min2 and arr[i]>min1:
		min2=arr[i]
print ("2nd max= ", max2)
print ("2nd min= ", min2)
