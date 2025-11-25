
def if_even(number):
    """
    returns true if the num is even else return false
    :param number:
    :return:
    """
    return number % 2 == 0

def if_odd(number):
    """
    returns true if the num is even else return false
    :param number:
    :return:
    """
    return number % 2 != 0
#
if __name__ !='__main__':
    print("dtc file successfully imported.")

if __name__=='__main__':
    number= int(input("enter a number:"))
    print(f" number:{number} is even=> {if_even(number)}")
