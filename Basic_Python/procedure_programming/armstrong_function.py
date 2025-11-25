def check_armstrong(number):
    total: int = 0
    temp_number:int = number
    length = len(str(number))


    for i in range(length):
        remainder, quotient = temp_number % 10, temp_number // 10
        total = total + (remainder ** length)
        temp_number = quotient

        if quotient == 0:
            break
    # while True:
    #     remainder, quotient = temp_number % 10, temp_number // 10
    #     total = total + (remainder ** length)
    #     temp_number = quotient
    #
    #     if quotient == 0:
    #         break

    return total == number

number: int  = int(input("Enter a number: "))
result = check_armstrong(number)

if result:
    print(f"Number {number} is an Armstrong Number")
else:
    print(f"Number {number} is not an Armstrong Number")
