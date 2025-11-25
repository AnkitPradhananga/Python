def custom_sum( *args):
    total = 0
    for value in args:
        total += value

    return total

def square(number:int | float) -> int | float:
    return number ** 2

def custom_apply(func, *args):
    applied_list = list()
    for value in args:
        applied_list.append(
            func(value)
        )
    return applied_list

# print(f"Total => {custom_apply(
#     lambda x: x**2
#     , 1,2,3,4,5,4,4
#     )}")

print(f"Total => {custom_apply(
    lambda x: (x[0] + x[1])**2
    , (1,2),(3,4),(5,4),(4,1)
    )}")