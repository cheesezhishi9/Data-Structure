def expression(lissy):
    # Please write your code here
    res = []

    def add(lst):
        lst[1] = str(lst[0])+'+'+str(lst[1])
        return[lst[1]]

    def multiply(lst):
        lst[1] = str(lst[0])+'*'+str(lst[1])
        return[lst[1]]

    def substraction(lst):
        lst[1] = str(lst[0])+'-'+str(lst[1])
        return[lst[1]]
    
    if len(lissy) == 1:
        return [str(lissy[0])]
        
    else:
        tmp = expression(add(lissy[0:2]) + lissy[2:]) + expression(multiply(lissy[0:2]) + lissy[2:]) + expression(substraction(lissy[0:2]) + lissy[2:])
        for item in tmp:
            res.append(item)
    
    return res

     


def main():
    print(expression([1,2,3]))  # Should print:
    # ["1+2+3", "1+2-3", "1+2*3", "1-2+3", "1-2-3", "1-2*3", "1*2+3", "1*2-3", "1*2*3"]

    print(expression([8,9])) # Should print:
    # ["8+9", "8*9", "8-9"]
    
if __name__ == '__main__':
    main()
