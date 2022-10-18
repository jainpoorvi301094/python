#itertolls: product, permutation, combinations, acccumulate, groupby, and infinite iterators
#product
from itertools import product
from itertools import permutations
from itertools import combinations
from itertools import combinations_with_replacement
from itertools import accumulate
from itertools import groupby


a=[1, 2]
b=[3, 4]

prod=product(a,b)
print(list(prod))

c=[1,2,3]
permutate=permutations(c)
print(list(permutate))

combination=combinations(c,2) #where 2 is the length
print(list(combination))

comb_wr=combinations_with_replacement(c,2)
print(list(comb_wr))

#acc=accumulate(c)
acc=accumulate(c, func=max)
print(c)
print(list(acc))

persons=[{"name":"poorvi", "age":27},{"name":"pari", "age":27},{"name":"pritishtha", "age":7} ]
group_obj=groupby(persons, key=lambda x:x["age"])
for key, value in group_obj:
    print(key, list(value))

from itertools import count
for i in count(10):
    print(i)
    if i==15:
        break

from itertools import cycle

d=[1,2,3]
for i in cycle(d):
    print(i)
    if i==3:
        break

from itertools import repeat
d=[1,2,3]
for i in repeat(3, 1):
    print(i)
