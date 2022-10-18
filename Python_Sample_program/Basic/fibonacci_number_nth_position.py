def fiboIter(num):
    prev_number=0
    current_number=1
    for i in range(1, num):
        preprev_number=prev_number
        prev_number=current_number
        current_number=preprev_number+prev_number

    return current_number

def fiborecur(num):
    if num==0:
        return 0
    elif num==1:
        return 1
    else:
        return fiborecur(num-1)+fiborecur(num-2)

if __name__=='__main__':
    num=int(input("Input Number"))

    print(fiborecur(num))
    print(fiboIter(num))
