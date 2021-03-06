# @decorator
from time import time


def my_decorator(func):
    def wrap_function(*args, **kwargs):
        print('\n++++++++++')
        func(*args, **kwargs)
        print('**********')
    return wrap_function


@my_decorator  # super bust our hello function.
def hello(greeting, name='Diego'):
    print(greeting, name)


hello('Hi', 'Diego')


@my_decorator
def bye(greeting, name='Diego'):
    print(greeting, name)


bye('Goodbye', 'Diego')


# EXERCISE
print('\n\nEXERCISE:\n\n')


def performance(func):
    def wrapped(*args, **kwars):
        time_1 = time()
        result = func(*args, **kwars)
        time_2 = time()
        print(f'took {time_2 - time_1} ms')
        return result
    return wrapped

# GENERATOR + DECORATOR
@performance
def long_time():
    for i in range(100000000): # range is the generator.
        i * 5


long_time()


@performance
def long_time_2():
    for i in list(range(100000000)):
        i * 5


long_time_2()
