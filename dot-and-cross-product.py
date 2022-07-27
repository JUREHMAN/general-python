#Components of the first vector
from re import I


c1v1 = float(input("Please Enter the first component of the first vector:\n"))
c2v1 = float(input("Please Ente the second component of the first vector:\n"))
c3v1 = float(input("Please Enter the third component of the first vector:\n"))

#components of the second vector
c1v2 = float(input("Please Enter the first component of the second vector:\n"))
c2v2 = float(input("Please Enter the second component of the second vector:\n"))
c3v2 = float(input("Please Enter the third component of the second vector:\n "))

#choice for dot or cross product
n = int(input("Please Enter\n0 for the Dot/Scalar product\n1 for the Cross/Vector product:\n"))

#for dot product
if n == 0:
    sp = c1v1 * c1v2 + c2v1 * c2v2 + c3v1 * c3v2
    print("The Dot product of your given vectors is ",sp,"units")

#for cross product
elif n == 1:
    cp1 = (c2v1 * c3v2 - c3v1 * c2v2)
    cp2 = - (c1v1 * c3v2 - c3v1 * c1v2)
    cp3 = (c1v1 * c2v2 - c1v2 * c2v1)

    
    print("The Cross product of your given vectors is ",cp1,"i +",cp2,"j +",cp3,"k units")

else:
    print("Unexpected Error")