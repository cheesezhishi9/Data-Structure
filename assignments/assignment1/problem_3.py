class Fraction:
    """
       This class provides arithmetic functions for handling fractions.
       Implement the given methods as described in the worksheet.
    """

    # Please write your code here
    def __init__(self,x,y):
        if y == 0:
            raise ZeroDivisionError
        else:
            self.x = x
            self.y = y
    
    
    def __add__(self,other):
        denominator1 = self.y
        denominator2 = other.y
        self.y *= denominator2
        self.x *= denominator2
        other.x *= denominator1
        res = Fraction(self.x + other.x,self.y)
        return res
    
    def __iadd__(self,other):
        denominator1 = self.y
        denominator2 = other.y
        self.x = self.x * denominator2 + other.x * denominator1
        self.y *= denominator2
        return self
        
        
    def __sub__(self,other):
        denominator1 = self.y
        denominator2 = other.y
        self.y *= denominator2
        self.x *= denominator2
        other.x *= denominator1
        res = Fraction(self.x - other.x,self.y)
        return res
        
    
    def __mul__(self,other):
        res = Fraction(self.x,self.y)
        res.x *= other.x
        res.y *= other.y
        return res
    
    def __truediv__(self,other):
        if other.x == 0:
            raise ZeroDivisionError
        else:
            res = Fraction(self.x * other.y,other.x*self.y)
        return res
    
    def __eq__(self,other):
        if self.x * other.y == self.y * other.x:
            return True
        else:
            return False
    
    def __str__(self):
        return str(self.x)+'/'+str(self.y)


def main():
    f1 = Fraction(1, 5)
    f2 = Fraction(2, 5)
    f3 = Fraction(3, 6)

    res = f1 + f2  # should print "3/5"
    print(res)

    res = f1 - f2  # should print "-1/5"
    print(res)

    res = f1 * f2  # should print "2/25"
    print(res)

    res = f1 + f3  # should print "7/10"
    print(res)

    res = f1 / f2  # should print "1/2"
    print(res)


if __name__ == '__main__':
    main()
