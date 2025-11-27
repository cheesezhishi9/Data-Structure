def reshape_array(arr, new_shape):
    # please write your code here
    k = new_shape[0]
    m = new_shape[1]
    n = new_shape[2]
    reshaped_array = [[[0] * n for _ in range(m)] for _ in range(k)]


    def next(arr,idx):
        k = len(arr)
        m = len(arr[0])
        n = len(arr[0][0])
        if idx < n:
            return arr[0][0][idx]
        elif n <= idx < m * n:
            idx_m = idx // n
            idx_n = idx - (idx // n) * n
            return arr[0][idx_m][idx_n]
        elif idx >= m * n:
            idx_k = idx // (m * n)
            idx_m = ((idx - m * n) % (m * n)) // n
            idx_n = ((idx - m * n) % (m * n)) % n
            return arr[idx_k][idx_m][idx_n]
        
    idx = 0
    for i in range(k):
        for j in range(m):
            for p in range(n):
                reshaped_array[i][j][p] = next(arr,idx)
                idx += 1
        
    return reshaped_array



                




    


def main():
    # (4x3x2) 3D array
    original_array = [
        [[1, 2], [3, 4], [5, 6]],
        [[7, 8], [9, 10], [11, 12]],
        [[13, 14], [15, 16], [17, 18]],
        [[19, 20], [21, 22], [23, 24]]
    ]

    new_shape = (2, 3, 4)  # Desired new shape
    reshaped_array = reshape_array(original_array, new_shape)
    print("Original array:", original_array)  # should print: [[[1, 2], [3, 4], [5, 6]], [[7, 8], [9, 10], [11, 12]], [[13, 14], [15, 16], [17, 18]], [[19, 20], [21, 22], [23, 24]]]
    print("Reshaped array:", reshaped_array)  # should print: [[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], [[13, 14, 15, 16], [17, 18, 19, 20], [21, 22, 23, 24]]]

    new_shape = (4, 3, 2)  # Desired new shape (original shape)
    reshaped_array = reshape_array(reshaped_array, new_shape)
    print("Original array:", original_array)  # should print: [[[1, 2], [3, 4], [5, 6]], [[7, 8], [9, 10], [11, 12]], [[13, 14], [15, 16], [17, 18]], [[19, 20], [21, 22], [23, 24]]]
    print("Reshaped array:", reshaped_array)  # should print: [[[1, 2], [3, 4], [5, 6]], [[7, 8], [9, 10], [11, 12]], [[13, 14], [15, 16], [17, 18]], [[19, 20], [21, 22], [23, 24]]]


if __name__ == '__main__':
    main()
