# FizzBuzz fizz on every number divisable by 3, Buzz on every by 5, FizzBuzz if 3 and 5

for numbers in range(1, 101):
    if numbers % 3 == 0 and numbers % 5 == 0:
        print("FizzBuzz")
    if numbers % 3 == 0:
        print("Fizz")
    if numbers % 5 == 0:
        print("Buzz")
    else:
        print(numbers)
    