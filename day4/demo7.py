# Create a 3x4 matrix as list of lists
matrix_list = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

# Create a 3x4 matrix as tuple of tuples
matrix_tuple = (
    (12, 11, 10, 9),
    (8, 7, 6, 5),
    (4, 3, 2, 1)
)

# Function to calculate addition and subtraction
def add_sub_matrices(mat1, mat2):
    addition = []
    subtraction = []

    for i in range(len(mat1)):
        add_row = []
        sub_row = []
        for j in range(len(mat1[0])):
            add_row.append(mat1[i][j] + mat2[i][j])
            sub_row.append(mat1[i][j] - mat2[i][j])
        addition.append(add_row)
        subtraction.append(sub_row)

    return addition, subtraction


# Main
add_result, sub_result = add_sub_matrices(matrix_list, matrix_tuple)

print("Addition Result:")
for row in add_result:
    print(row)

print("\nSubtraction Result:")
for row in sub_result:
    print(row)
