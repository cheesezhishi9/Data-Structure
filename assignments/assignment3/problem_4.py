def solver(maze):
    # Please write your code here
    res = [(0,0)]
    coord_x = len(maze) - 1
    coord_y = len(maze[0]) - 1

    def right_way(i,j):
        if 0 <= i <= coord_x and 0 <= j <= coord_y:
            if maze[i][j] == 1:
                return True
        else:
            return False
        
    def move_puzzle(i,j):
        if i == coord_x and j == coord_y:
            return True
        maze[i][j] = 0
        
        if i + 1 <= coord_x and right_way(i + 1,j):
            res.append((i + 1, j))
            if move_puzzle(i + 1, j):
                return True
            res.pop(-1)
        
        if j + 1 <= coord_y and right_way(i,j + 1):
            res.append((i, j + 1))
            if move_puzzle(i , j + 1):
                return True
            res.pop(-1)
        
        if i - 1 >= 0 and right_way(i - 1, j):
            res.append((i - 1, j))
            if move_puzzle(i - 1,j):
                return True
            res.pop(-1)
        
        if j - 1 >= 0 and right_way(i, j - 1):
            res.append((i , j - 1))
            if move_puzzle(i, j - 1):
                return True
            res.pop(-1)
        
        maze[i][j] = 1
        return False
    

    if move_puzzle(0,0) == False:
        return []
    
    return res
    
    


def main():
    res = solver([[1, 0, 1, 1, 1],
                  [1, 0, 1, 0, 1],
                  [1, 0, 1, 0, 1],
                  [1, 1, 1, 0, 1]])

    print(res)  # Should print
    # [(0, 0), (1, 0), (2, 0), (3, 0), (3, 1), (3, 2), (2, 2), (1, 2), (0, 2), (0, 3), (0, 4), (1, 4), (2, 4), (3, 4)]

    res = solver([[1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
                  [0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1],
                  [1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1],
                  [1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1],
                  [1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1],
                  [1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1],
                  [1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1],
                  [1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1],
                  [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1],
                  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]])

    print(res)  # Should print
    # [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2), (3, 2), (4, 2), (5, 2), (5, 3), (5, 4), (4, 4), (3, 4), (2, 4), (1, 4),
    # (0, 4), (0, 5), (0, 6), (0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (4, 8), (4, 9), (4, 10), (3, 10), (2, 10),
    # (2, 11), (2, 12), (3, 12), (4, 12), (5, 12), (6, 12), (7, 12), (8, 12), (9, 12), (9, 13), (9, 14)]


if __name__ == '__main__':
    main()
