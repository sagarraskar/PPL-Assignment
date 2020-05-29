import numpy as np




def luDecomposition(mat, n):
    lower = np.zeros((n,n), dtype='int32')
    upper = np.zeros((n,n), dtype='int32')

    for i in range(n):
        for k in range(i, n):
            sum = 0
            for j in range(i):
                sum += (lower[i][j] * upper[j][k])

            upper[i][k] = mat[i][k] - sum

        for k in range(i, n):
            if (i == k):
                lower[i][i] = 1
            else:
                sum = 0
                for j in range(i):
                    sum += (lower[k][j] * upper[j][i])

                lower[k][i] = int((mat[k][i] - sum) /
                                  upper[i][i])

    print(lower, "\n\n", upper)

mat = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]

luDecomposition(mat, 3)