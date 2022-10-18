import random
list1=[1,2,3,4,5,6]

random_number_from_list=random.choice(list1)
print(random_number_from_list)

#Shuffle
print(list1)
shuffle1=random.shuffle(list1)
print(list1)
shuffle2=random.shuffle(list1)
print(list1)

#randint
r1=random.randint(1,10)
print(r1)

#seed
random.seed(5)
print(random.random())

def plus_one(number):
    return number + 1

add_one = plus_one
print(add_one(5))

def plus_one(number):
    return number + 1

def function_call(function):
    number_to_add = 6
    return function(number_to_add)

print(function_call(plus_one))

