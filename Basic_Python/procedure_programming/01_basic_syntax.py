from dtc_math import if_even

def sum_four(n1, n2 ,n3 , n4 ):
    total = n1+n2+n3+n4
    return total

integers = []
# for i in range(4):
#     integers.append(int(input(f"enter number{i+1}:")))
#     value = int(input(f"enter{i+1}:"))
#     integers.append(value)

# meth3:
value = input("enter numbers in sequence n1,n2,n3,n4:")
numbers = value.split(',')
print(numbers)

for i in range(len(numbers)):
    numbers[i] = int(numbers[i])

# sum_value = sum_four(*numbers)
sum_value = sum_four (numbers[0],numbers[1],numbers[2],numbers[3] )
print(if_even(sum_value))
# sum_four(1,2,n4=1,n3=2)

print(f"num:{sum_value} is even {if_even(sum_value)}")