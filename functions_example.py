def add(num1:int, num2:int)->int:
    num3=num1+num2

    return num3

num1,num2=4,7
sum=add(num1,num2)
print(f"the summation is:{sum}")

# Python program to illustrate
# *args for variable number of arguments


def myFun(*argv):
	for arg in argv:
		print(arg)


myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')


# Python program to illustrate
# *kwargs for variable number of keyword arguments


def myFun(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))


# Driver code
myFun(first='Geeks', mid='for', last='Geeks')


# A simple Python function to check
# whether x is even or odd


def evenOdd(x):
    """Function to check if the number is even or odd"""

    if (x % 2 == 0):
        print("even")
    else:
        print("odd")


# Driver code to call the function
print(evenOdd.__doc__)
evenOdd(5)

def myFun(arg1, **kwargs):
	for key, value in kwargs.items():
		print("%s == %s" % (key, value))


# Driver code
myFun("Hi", first='Geeks', mid='for', last='Geeks')


class car():  # defining car class
    def __init__(self, *args):  # args receives unlimited no. of arguments as an array
        self.speed = args[0]  # access args index like array does
        self.color = args[1]


# creating objects of car class

audi = car(200, 'red')
bmw = car(250, 'black')
mb = car(190, 'white')

print(audi.color)
print(bmw.speed)

class Car1():
    def __init__(self,**kwargs):
        self.speed=kwargs['s']
        self.color=kwargs['c']

audi1=Car1(s=250,c='white')
Bmw=Car1(s=350,c='black')

print(audi1.speed)
print(Bmw.color)

# Python program to illustrate functions
# can be passed as arguments to other functions
def shout(text):
	return text.upper()

def whisper(text):
	return text.lower()

def greet(func):
	# storing the function in a variable
	greeting = func("""Hi, I am created by a function passed as an argument.""")
	print (greeting)

greet(shout)
greet(whisper)


import time
import math

def calculate_time(func):
    def inner1(*args, **kwargs):
        begin=time.time()

        func(*args, **kwargs)

        end=time.time()
        print("total time taken is:", func.__name__, end-begin)

    return inner1

calculate_time
def factorial_number(num):

    #time.sleep(10)
    print(math.factorial(num))

factorial_number(20)

# Factorial program with memoization using
# decorators.

# A decorator function for function 'f' passed
# as parameter
memory = { }
def memoization_factorial(f):
# This inner function has access to memory
# and 'f'
    def inner(num):
        if num not in memory:
            memory[num]=f(num)
            print("result saved in memory")

        else:
            print("returning result from saved memory")
        return memory[num]
    return inner

@memoization_factorial
def facto(num):
    if num==1:
        return 1
    else:
        return num*facto(num-1)

print(facto(10))

