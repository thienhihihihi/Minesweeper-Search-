def convert_zero_to_o(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                matrix[i][j] = 'O'
    return matrix

# Ví dụ sử dụng
matrix = [
   [0,-1,2,1,0,0,2,0,0,2,1,0,2,-1,3,0,2,0,0,0],
            [0,2,3,-1,0,-1,5,-1,-1,-1,0,0,3,-1,-1,0,-1,-1,-1,2],
            [-1,3,0,-1,6,-1,-1,-1,5,3,0,1,-1,4,4,0,5,-1,4,-1],
            [3,-1,-1,-1,4,-1,0,3,-1,1,0,0,0,4,-1,-1,-1,0,0,0],
            [0,-1,0,0,0,0,0,2,0,0,0,1,-1,-1,3,0,0,0,1,-1],
            [0,1,1,1,-1,3,-1,0,0,0,0,0,0,4,3,0,1,0,1,0]
]


converted_matrix = convert_zero_to_o(matrix)
print(converted_matrix)
