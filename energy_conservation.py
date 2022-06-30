"""
This is a simple program to check whether the mechanical energy is conserved or not....
It takes four parameters which are initial height, final height, initial velocity and final velocity.
By using work energy principle, this program determine whether the energy is conserved or not..
"""
#m = float(input("Please Enter the mass(in Kg) of the object..\n"))

hi = float(input("Please Enter the initial height(in m) of the object..\n"))
hf = float(input("Please Enter the final height(in m) of the object...\n"))
vi = float(input("Please Enter the initial speed(in m/s) of the object..\n"))
vf = float(input("Please Enter the final speed(in m/s) of the object...\n"))
g = 9.8

if 2 * g * (hi - hf) == vf**2 - vi**2:
    print("Mechanical Energy is conserved in this case..")
else:
    print("Mechanical Energy is not conserved in this case...")
	
 
