number: int  = int(input("Enter a number: "))
total:  int = 0
temp_number: int = number
length =  len(str(number))

while True:
    remainder, quotient = temp_number % 10, temp_number // 10
    total = total + (remainder ** length)
    temp_number = quotient

    if quotient == 0:
        break

'''
iteration 1
temp -> 153, total -> 0, R -> 3, Q-> 15: T->Q, Total->
temp -> 15, R -> 5, Q ->1 : T->1
temp -> 1, R -> 1,Q -> 0:T ->Q

#decision total =  number
153/10 -> 15.3
'''
if total == number:
    print(f"Number {number} is an Armstrong Number")
else:
    print(f"Number {number} is not an Armstrong Number")
