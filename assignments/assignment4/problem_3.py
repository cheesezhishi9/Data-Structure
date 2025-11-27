def count_connected(voxel_grid):
    # please write your code here
    count = 0
    x = len(voxel_grid)
    y = len(voxel_grid[0])
    z = len(voxel_grid[0][0])
    
    included = [[[False for _ in range(z)] for _ in range(y)] for _ in range(x)]

    def if_connected(i,j,p):
        if not (0 <= i < x and 0 <= j < y and 0 <= p < z) or included[i][j][p] or voxel_grid[i][j][p] == 0:
            return
        else:
            included[i][j][p] = True
            if_connected(i + 1,j,p)
            if_connected(i,j + 1,p)
            if_connected(i,j,p + 1)
            if_connected(i - 1,j,p)
            if_connected(i,j - 1,p)
            if_connected(i,j,p - 1)

    for i in range(x):
        for j in range(y):
            for p in range(z):
                if voxel_grid[i][j][p] == 1:
                    if not included[i][j][p]:
                        if_connected(i,j,p)
                        count += 1
    
    
    return count



def visualize(voxel_grid):
    """
    This is a given method for visualizing a provided voxel-grid.
    You cannot change this function.
    """
    import numpy as np
    import matplotlib.pyplot as plt

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.voxels(np.array(voxel_grid))
    plt.show()


def main():
    # multidimensional representation of a single voxel.
    single_cube = [
        [
            [1]
        ]
    ]
    # Uncomment the following line of code to visualize the 3d-array using matplotlib.
    # You need to comment this line when submitting your solution to gradescope to prevent errors.
    # visualize(single_cube)
    print(count_connected(single_cube))  # Should print the integer "1"

    # multidimensional representation of two cube-like components.
    two_cube_like_components = [
        [
            [1, 1, 0, 0, 0],
            [1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ], [
            [1, 1, 0, 0, 0],
            [1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ], [
            [1, 0, 0, 0, 0],
            [1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1],
            [0, 0, 0, 0, 1]
        ], [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 1, 1],
            [0, 0, 0, 1, 1]
        ], [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 1, 1],
            [0, 0, 0, 1, 1]
        ]
    ]
    # Uncomment the following line of code to visualize the 3d-array using matplotlib.
    # You need to comment this line when submitting your solution to gradescope to prevent errors.
    # visualize(two_cube_like_components)
    print(count_connected(two_cube_like_components))  # Should print the integer "2"

    # multidimensional representation of 6 bars in diagonal.
    six_bars = [
        [
            [1, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0],
            [0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 1]
        ],
        [
            [0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0],
            [0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 1]
        ],
        [
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0],
            [0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 1]
        ],
        [
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 1]
        ],
        [
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 1]
        ],
        [
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1]
        ]
    ]
    # Uncomment the following line of code to visualize the 3d-array using matplotlib.
    # You need to comment this line when submitting your solution to gradescope to prevent errors.
    # visualize(six_bars)
    print(count_connected(six_bars))  # Should print the integer "6"

    # multidimensional representation of 3 connected blocks.
    connected_blocks = [
        [
            [1, 1, 0, 0],
            [1, 1, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
        ],
        [
            [0, 0, 0, 0],
            [0, 1, 1, 0],
            [0, 1, 1, 0],
            [0, 0, 0, 0],
        ],
        [
            [0, 0, 0, 0],
            [0, 1, 1, 0],
            [0, 1, 1, 0],
            [0, 0, 0, 0],
        ],
        [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 1, 1],
            [0, 0, 1, 1],
        ]
    ]
    # Uncomment the following line of code to visualize the 3d-array using matplotlib.
    # You need to comment this line when submitting your solution to gradescope to prevent errors.
    # visualize(connected_blocks)
    print(count_connected(connected_blocks))  # Should print the integer "1"

    # multidimensional representation of 2 bars.
    two_bars = [
        [
            [1, 0],
        ], [
            [0, 1],
        ]
    ]
    # Uncomment the following line of code to visualize the 3d-array using matplotlib.
    # You need to comment this line when submitting your solution to gradescope to prevent errors.
    # visualize(two_bars)
    print(count_connected(two_bars))  # Should print the integer "2"

    # multidimensional representation of 2 bars (2).
    two_bars_2 = [
        [
            [1, 0, 0],
            [1, 0, 0],
            [1, 0, 0],
        ], [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
        ], [
            [0, 0, 0],
            [0, 0, 0],
            [1, 1, 1],
        ]
    ]
    # Uncomment the following line of code to visualize the 3d-array using matplotlib.
    # You need to comment this line when submitting your solution to gradescope to prevent errors.
    # visualize(two_bars_2)
    print(count_connected(two_bars_2))  # Should print the integer "2"

    # multidimensional representation of 3 connected componentes.
    connected_3 = [
        [
            [1, 0, 0],
            [1, 0, 0],
            [1, 0, 0],
        ], [
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 1],
        ], [
            [0, 0, 0],
            [0, 0, 0],
            [1, 1, 1],
        ]
    ]
    # Uncomment the following line of code to visualize the 3d-array using matplotlib.
    # You need to comment this line when submitting your solution to gradescope to prevent errors.
    # visualize(connected_3)
    print(count_connected(connected_3))  # Should print the integer "3"

    # multidimensional representation of a partial wireframe.
    partial_wireframe = [
        [
            [1, 1, 1, 1, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 0, 0, 1],
            [1, 1, 1, 1, 1],
        ], [
            [1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [1, 0, 0, 0, 1],
        ], [
            [1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [1, 0, 0, 0, 1],
        ], [
            [1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [1, 0, 0, 0, 1],
        ], [
            [1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [1, 0, 0, 0, 1],
        ], [
            [1, 1, 0, 0, 0],
            [1, 0, 0, 0, 0],
            [1, 0, 0, 0, 0],
            [1, 0, 0, 0, 0],
            [1, 1, 1, 1, 1],
        ]
    ]
    # Uncomment the following line of code to visualize the 3d-array using matplotlib.
    # You need to comment this line when submitting your solution to gradescope to prevent errors.
    # visualize(partial_wireframe)
    print(count_connected(partial_wireframe))  # Should print the integer "1"


if __name__ == "__main__":
    main()
