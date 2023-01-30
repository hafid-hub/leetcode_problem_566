def reshape_the_matrix(mat: list[list[int]], new_row: int, new_col: int) -> list[list[int]]:

    #STEP 1: check if we can do that (reshape the matrix). If not, return
    # the original matrix.
    # We can only reshape the matrix if the product of the length of its column
    # and its row is equal to the product of new_row and new_col.
    length_row = len(mat)
    length_col = len(mat[0])
    if length_col * length_row != new_row * new_col:
        return mat

    #STEP 2: initialization.
    new_matrix = []
    temporay_list = []
    i = 0

    #STEP 3: create a temporary list that save a portion of the matrix
    #that has a length lesser than the number of the columns in the new
    #matrix. After that we append the new matrix by the portion of that
    # temporary list that has the same length as the number of columns
    # in the new matrix.
    # This same portion of this portion that we add is deleted from
    # the temporary list.
    while i < length_row or temporay_list:
        while len(temporay_list) < new_col:
            temporay_list = temporay_list + mat[i]
            i = i + 1
        new_matrix.append(temporay_list[:new_col])
        temporay_list = temporay_list[new_col:]
    return new_matrix

### Testing the code ###

mat1, new_row1, new_col1 = [[1,2],[3,4]], 1, 4
mat2, new_row2, new_col2 = [[1,2],[3,4]], 2, 2
mat3, new_row3, new_col3 = [[1,5,7,8], [2,4,1,9], [12,5,4,6], [1,3,2,1], [6,7,8,3],[3,10,1,6]], 8, 3
mat4, new_row4, new_col4 = [[1,5,7,8], [2,4,1,9], [12,5,4,6], [1,3,2,1], [6,7,8,3],[3,10,1,6]], 3, 8
mat5, new_row5, new_col5 = [[1,2,3],[4,5,6]], 3, 2
mat6, new_row6, new_col6 = [[1,2],[3,4]], 4, 1
mat7, new_row7, new_col7 = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]], 25, 1

print(reshape_the_matrix(mat1, new_row1, new_col1))
print("-----------------------------")
print(reshape_the_matrix(mat2, new_row2, new_col2))
print("-----------------------------")
print(reshape_the_matrix(mat3, new_row3, new_col3))
print("-----------------------------")
print(reshape_the_matrix(mat4, new_row4, new_col4))
print("-----------------------------")
print(reshape_the_matrix(mat5, new_row5, new_col5))
print("-----------------------------")
print(reshape_the_matrix(mat6, new_row6, new_col6))
print("-----------------------------")
print(reshape_the_matrix(mat7, new_row7, new_col7))




