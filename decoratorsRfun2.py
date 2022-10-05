def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner

def ordinary():
    print("I'm ordinary")


print(ordinary())
# let's decorate this ordinary function
pretty = make_pretty(ordinary)
print(pretty())

