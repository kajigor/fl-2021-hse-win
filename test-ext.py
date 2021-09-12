import math

#this is a comment

class User:
    firstname = ""
    lastname = ""

    def __init__(self, f, l):
        self.firstname = f
        self.lastname = l

def f():
    user = User("Alex", "Buyan")
    print(user.firstname + user.lastname)
    return 1.1

a = f()
b = 100

print(a + b)
