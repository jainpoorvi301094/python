start=input("Start Position")
start=int(start)
end=input("End position")
end=int(end)

for num in range(start, end+1):
    if num>0:
        for i in range(2, num):
            if (num%i)==0:
               break
        else:
            print(num)


