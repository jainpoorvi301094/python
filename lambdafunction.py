#lambda arguments: expression
#with single argument
add10= lambda x:x+10
print(add10(5))

#with multiple arguments
mul= lambda x,y:x*y
print(mul(5,8))

#Sort Method using lambda
points_2d=[(1,5),(2,6),(5,-1),(7,2)]
points_2d_sorted_with_key=sorted(points_2d)
points_2d_sorted_with_value=sorted(points_2d, key=lambda x:x[1])
points_2d_sorted_with_sumof_key_value=sorted(points_2d,key=lambda x:x[0]+x[1])

print(points_2d)
print(points_2d_sorted_with_key)
print(points_2d_sorted_with_value)
print(points_2d_sorted_with_sumof_key_value)

#map(fun, seq)
a=[1,2,4,8,7]
b=map(lambda x: x*2, a)
print(list(b))

c=[x*2 for x in a] #List Comprehensive
print(c)

#filter Method
d=filter(lambda x:x%2==0, a)
print(list(d))

e=[x for x in a if x%2==0] #List Comprehensive
print(e)

#reduce function
from functools import reduce
f=reduce(lambda x,y:x*y, a)
print(f)
