local_val = "magical unicorns"
def square(x):
    return x * x
class User:
    def __init__(self, name):
        self.name = name
    def say_hello(self):
        return "hello"

print(square(5))
user = User("Sachiko")
print(user.name)
print(user.say_hello())