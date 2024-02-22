import math
def rad(n):
    return math.radians(n)  
#print(rad(int(input())))

#########################

def trap(h,base,Base):
    return (base+Base)/2*h
# print(trap(5,5,6))

#########################

def area_pol(n,l):
    return 1/4*n*l*l/(math.tan(rad(180/n)))
# print(area_pol(4,25))

#########################

def area_pal(a,b):
    return a*b

print(area_pal(5,6))
