from typing import Callable

def logger(func: Callable) -> Callable:
    """
     step 1: logger bata decorate-> logger bhitra function pass
     step 2: returs the wrapper function => logic of logging
    :param func:
    :return:
    """
    def wrapper(*args, **kwargs):
        print(f"{func.__name__} has been invoked with parameters: {args}, {kwargs}")
        return func(*args, **kwargs)

    return wrapper

if __name__=="__main__":
    @logger
    def  func1():
        print("Func 1")

    @logger
    def func2(*args, **kwargs):
        print("Func 2 invoked.")

func1()
func2(1,2,3,4,5,6, test = True, name = "database connection")
func1()