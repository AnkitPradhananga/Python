from typing import Callable


def maker():
    embigger = 2
    def adder(a,b):
        return a+b+embigger

    return adder
#increment value by 2,3 ,4
# def increase_2(value):
#     return value + 2
#
# def increase_3(value):
#     return value + 3


#lambda x : x+2 #cost of compute and storage

def generate_increase(increment: int) -> Callable
    def inner (value):
        return value + increment
    return inner

increase_by_2 = generate_increase(2)
increase_by_3 = generate_increase(3)

print(f"output => {maker()(4,5)}")