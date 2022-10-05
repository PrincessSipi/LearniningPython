def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner

@ make_pretty
def ordinary():
    print("I'm ordinary")

print(ordinary())

