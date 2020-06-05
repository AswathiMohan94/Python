import cmath
a=float(input("enter the value of a : "))
b=float(input("enter the value of b : "))
c=float(input("enter the value of c : "))
delta=(b**2)-(4*a*b)
root1=(-b+cmath.sqrt(delta))/(2*a)
root2=(-b-cmath.sqrt(delta))/(2*a)
print("root1 : ",root1)
print("root2 : ",root2)
 
