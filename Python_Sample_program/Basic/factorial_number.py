'''def fact(num): #Ternary Operator
    return 1 if num==1 else num*fact(num-1)

print(fact(5))'''

#Simple method

def fact(n):
    if n==0 or n==1:
        return 1
    else:
        fact = 1
        while (n > 1):
            fact *= n
            n -= 1
        return fact

print(fact(5))


