import math

def isperfectsqart(x):
    s=int(math.sqrt(x))
    return s*s==x

def isfibonacci(n):
    return isperfectsqart(5*n*n+4) or isperfectsqart(5*n*n-4)

for i in range(1,11):
    if isfibonacci(i)==True:
        print(i, "is a fibonacci number")
    else:
        print(i, "is not a fibonacci number")