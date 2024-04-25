import math
def calculatecosine(l):
    return (l/math.sqrt(0.00825**2+l**2))

# arr = map(float,input().split())# 0.0419 0.0297 0.0338 0.0344 0.0347 0.0348 0.034 0.0338 0.034 0.0336
arr = [0.6,0.81,0.96,1.01,1.03,1.02,1.01,0.98,0.91,0.79,0.42]

x = -0.025
for i in arr:
    w = 2000
    l = 0.047
    M = 4*math.pi*(10**(-7))
    n = w/l
    I = 0.2
    
    num = M*n*I/2*(calculatecosine(x-l/2)-calculatecosine(x+l/2))
    print(f'{num*1000}:{x}')
    x+=0.005