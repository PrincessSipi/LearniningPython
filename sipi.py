print("hello")
# I'M GOING TO DEFINE A METHOD

class Children:

    def __init__(self, name , age , height):

        self.name: str = name
        self.age: int = age
        self.height: float = height
        print("My name is {} I am {} years old. I am {} metres, tall".format(self.name, self.age, self.height))


c1 = Children("Sammy", 10, 1.2)
c2 = Children("Charlie", 14, 1.5)
c3 = Children("Billy", 12, 1.3)






