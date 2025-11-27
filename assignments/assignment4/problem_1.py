def rotator(M,a,d):
    # Please write your code here

    if d == 'clockwise':
        if a == 90:
            for i in range(len(M)//2):
                for j in range(len(M)//2 + 1):
                    M[i][j],M[j][len(M)-1-i],M[len(M)-1-i][len(M)-1-j],M[len(M)-1-j][i] = M[len(M)-1-j][i],M[i][j],M[j][len(M)-1-i],M[len(M)-1-i][len(M)-1-j]
        elif a == 180:
            rotator(M,90,d)
            rotator(M,90,d)
        elif a == 270:
            rotator(M,90,d)
            rotator(M,90,d)
            rotator(M,90,d)
    elif d == 'anticlockwise':
        if a == 90:
            for i in range(len(M)//2):
               for j in range(len(M)//2 + 1):
                   M[i][j],M[j][len(M)-1-i],M[len(M)-1-i][len(M)-1-j],M[len(M)-1-j][i] = M[j][len(M)-1-i],M[len(M)-1-i][len(M)-1-j],M[len(M)-1-j][i], M[i][j]
        elif a == 180:
            rotator(M,90,d)
            rotator(M,90,d)
        elif a == 270:
            rotator(M,90,d)
            rotator(M,90,d)
            rotator(M,90,d)
    return M

        

            
            


        
                  

    


def main():
    mat = [ [ 1, 2, 3, 4, 5],
            [ 6, 7, 8, 9,10],
            [11,12,13,14,15],
            [16,17,18,19,20],
            [21,22,23,24,25] ]
    rotator(mat,90,"anticlockwise")
    print(mat)
    # should print [ [ 5,10,15,20,25],
            #        [ 4, 9,14,19,24],
            #        [ 3, 8,13,18,23],
            #        [ 2, 7,12,17,22],
            #        [ 1, 6,11,16,21] ]
    rotator(mat,0,"anticlockwise")
    print(mat)
    # should print [ [ 5,10,15,20,25],
            #        [ 4, 9,14,19,24],
            #        [ 3, 8,13,18,23],
            #        [ 2, 7,12,17,22],
            #        [ 1, 6,11,16,21] ]


if __name__ == '__main__':
    main()
