def rotate_image(matrix): 

    n=len(matrix)
    matrix.reverse()
    for i in range(n):
        for j in range(n):
            if i<j:
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]     

    return matrix 