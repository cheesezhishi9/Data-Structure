def is_palindrome(num):
    """
        A function to check whether an integer represents a palindrome in binary representation.
    """
    # Please write your code here
    if num < 0:
        return False
    
    bit = 0
    n = num

    while n > 0 :
        n >>= 1
        bit += 1
    
    for i in range(bit >> 2):
        num1 = (num >> i) & 1
        num2 = (num >> (bit-1-i)) & 1
        if num1 != num2:
            return False
    
    return True



def main():
    print(is_palindrome(220395))  # should print True
    # 220395 is 110101110011101011 in binary (valid palindrome)

    print(is_palindrome(1060))  # should print False
    # 220395 is 10000100100 in binary (not a palindrome)

    print(is_palindrome(75817))  # should print True
    # 220395 is 10010100000101001 in binary (valid palindrome)

    print(is_palindrome(820))  # should print False
    # 220395 is 1100110100 in binary (not a palindrome)

    print(is_palindrome(5557))  # should print True
    # 220395 is 1010110110101 in binary (valid palindrome)


if __name__ == '__main__':
    main()
