my_set={"january", "february","march", "march"}
#Set does not provide duplicate value, we can not access value based on index
for values in my_set:
    print(values)

my_set.add("may")
print(my_set)
my_set.remove("march")
print(my_set)