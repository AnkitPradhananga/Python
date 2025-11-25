num: int = int(input("Enter a number: "))

digits: int = len(str(num))
num_str: str = str(num)

total: int = 0

for digit in num_str:
    total = total + (int(digit) ** digits)


if total == num:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is NOT an Armstrong number.")
