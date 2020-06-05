str1=input("enter the 1st string : ")
str2=input("enter the 2nd string :")
n1=len(str1)
n2=len(str2)
#str3=str2
#str1=sorted(str1)
#str2=sorted(str2)
j=0
k=0
for i in range(0,n1):
	if((str1[i]==str2[i])and(n1==n2)):
	    j=1
	if((('a'<str1[i]>'z')==('a'<str2[i]>'z')) or (('A'<str1[i]>'Z')==('A'<str2[i]>'Z'))):
			k=1
if(k==1) and (j==0):
	print("anagram")
else:
	print ("not anagram")
		























