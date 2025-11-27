def add_numbers(b1, b2):
    """
       This functions performs a logical addition
    """

    # Please write your code here
    while b2 != 0:
        b3 = b1 & b2
        b1 ^=  b2
        b2 = b3 << 1
    return b1




def mul_numbers(b1, b2):
    """
       This functions performs a logical multiplication
    """

    # Please write your code here
    bit = 0
    num = 0
    while b1 > 0:
        if b1 & 1 != 0 :
            num = add_numbers(num, b2 << bit)
        bit += 1
        b1 >>= 1
    return num

def and_numbers(b1, b2):
    """
       This functions performs a logical and
    """

    # Please write your code here
    return b1 & b2


def or_numbers(b1, b2):
    """
       This functions performs a logical or
    """

    # Please write your code here
    return b1 | b2


def xor_numbers(b1, b2):
    """
       This functions performs a logical xor
    """

    # Please write your code here
    return b1 ^ b2


def main():
    print(add_numbers(3, 12))  # should return 15
    print(mul_numbers(3, 12))  # should return 36
    print(and_numbers(3, 12))  # should return 0
    print(or_numbers(3, 12))  # should return 15
    print(xor_numbers(3, 12))  # should return 15


if __name__ == '__main__':
    main()
