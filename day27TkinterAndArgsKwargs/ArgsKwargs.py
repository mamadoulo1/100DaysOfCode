

def add(*args):
    total = 0
    for n in args:
        total += n
    return total


def calculate(n, **kwargs):
    n += kwargs['add']
    n *= kwargs['mutiply']
    print(n)

class Car:
    def __init__(self, **kwargs):
        self.make = kwargs['make']
        self.model = kwargs['model']

my_car = Car(make="Nissan", model="GT-R")
print(my_car.model)


def bar(spam, eggs, toast='yes please!', ham=0):
    print(spam, eggs, toast, ham)


bar(toast='nah', spam=4, eggs=2)


def test(*args):
    print(args)


test(1, 2, 3, 5)


def all_aboard(a, *args, **kw):
    print(a, args, kw)


all_aboard(4, 7, 3, 0, x=10, y=64)