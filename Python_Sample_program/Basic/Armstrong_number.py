# python 3 program
# to check whether the given number is armstrong or not
# without using power function

n1=input("Usr Input:")
n=int(n1)
s=n
l=len(str(n))
sum1=0
while n!=0:
    r=n%10
    sum1=sum1+(r**l)
    n=n//10
if s==sum1:
    print("number is armstrong")
else:
    print("number is not armstrong")


