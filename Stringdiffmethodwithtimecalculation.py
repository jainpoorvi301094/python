from timeit import default_timer as timer
my_list=['1']*50000
my_string=' '

start=timer()
for i in my_list:
    my_string+=i
end=timer()
time=end-start
print(time)

start=timer()
my_string=''.join(my_list)
end=timer()
time1=end-start
print(time1)