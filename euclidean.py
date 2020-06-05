import cmath
import sys
print(sys.argv)
b=int(sys.argv[1])
c=int(sys.argv[2])
e=b**2
f=c**2
d=cmath.sqrt(e+f)
print ("euclidean distance = ",d)