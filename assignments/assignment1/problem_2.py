def encrypt(input_string, row_count):
    """
       This function receives a string and the row count for the matrix.
       Implement the algorithm and return the encrypted text.
    """

    # Please write your code here
    output_str = ''
    for i in range (0,len(input_string),2*(row_count-1)):
            output_str += input_string[i]
    for j in range(1,row_count):
        for i in range (0,len(input_string),2*(row_count-1)):
            if i + j != i+2*(row_count-1)-j:
                if i + j < len(input_string):
                    output_str += input_string[i+j]
                if i+2*(row_count-1)-j < len(input_string):
                    output_str += input_string[i+2*(row_count-1)-j]
            else:
                 if i + j < len(input_string):
                    output_str += input_string[i+j]
                 
    return output_str

            

def decrypt(input_string, row_count):
    """
       This function receives a string and the row count for the matrix.
       Implement the algorithm and return the decrypted text.
    """

    # Please write your code here
    res = [None] * len(input_string)
    index = 0
    for i in range(row_count):
        j = 0
        while i + j < len(input_string):
            res [i + j] = input_string [index]
            index += 1
            if 0 < i < row_count - 1 and j + 2*(row_count-1) - i < len(input_string):
                res [j + 2*(row_count-1) - i] = input_string[index]
                index += 1
            j += 2*(row_count-1)
    return ''.join(res)
            


        

        

    
        

    
        

        
    


def main():
    res = encrypt("DATASTRUCTURES", 3)
    print(res)  # should print DSCEAATUTRSTRU
    res = decrypt("DSCEAATUTRSTRU", 3)
    print(res)  # should print DATASTRUCTURES

    res = decrypt("CSORCMEIEPTECUN", 5)
    print(res)  # should print COMPUTERSCIENCE
    res = encrypt("COMPUTERSCIENCE", 5)
    print(res)  # should print CSORCMEIEPTECUN


if __name__ == '__main__':
    main()
