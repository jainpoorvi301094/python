# Return keyword
def fun():
    S = 0

    for i in range(10):
        S += i
    return S


print(fun())


def fun():
    S = 0

    for i in range(10):
        S += i
        yield S


for i in fun():
    print(fun(i))