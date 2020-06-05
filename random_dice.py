import random
def dice_roll():
	a=random.randint(1,6)
	return a
		
n=input("no of rolls : ")
i=1
k=0
list1=()
while(i<=n):
	j=dice_roll()
	i=i+1
	print(j)
	list1+=(j,)
print ("the list is : ",list1)



#g=set(list1)
#print "the elements used in this list are : ",g
h=max((list1),key=list1.count)
print ("the element with max repetation is : ",h)


	
	
