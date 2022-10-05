def inc(x):
    return x + 1

def dec(x):
    return x-1

def operate(func, x):
    result = func(x)
    return result

# we invoke the function as follows
print(operate(inc, 3))
print(operate(dec, 3))
