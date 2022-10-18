# Python3 Program to
# find sum of square
# of first n natural
# numbers
# Return the sum of
# square of first n
# natural numbers

def squarenumber(num):
    sm=0
    for i in range(1, num+1):
        sm = sm + (i*i)
    return sm

print(squarenumber(8))

