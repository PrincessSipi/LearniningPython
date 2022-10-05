def works_for_all(func):
    def inner(*args, **kwargs):
        print("I can decorate any function")
        return func(*args, **kwargs)
    return inner

def star(func):
    def inner(*args, **kwargs):
        print("*" * 30)
        return func(*args, **kwargs)
        print("*" * 30)
    return inner

def percent(func):
    def inner(*args, **kwargs):
        print("%" * 30)
        return func(*args, **kwargs)
        print("%" * 30)
    return inner

@star
@percent
def printer(msg):
    print(msg)


printer("Hello")


@percent
@star
def printer(msg):
    print(msg)    

printer("Hello")
