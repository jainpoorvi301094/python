def fibonacci(num):
    a=0
    b=1
    if num<0:
        print("incorrect input")
    if num==0:
        return a
    elif num==1:
        return b
    else:
        for i in range(2,num):
            c=a+b
            a=b
            b=c
            return b

print(fibonacci(20))