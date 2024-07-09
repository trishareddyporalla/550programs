'''r = int(input("Enter number of rows: "))
c = int(input("Enter number of columns: "))
A = []
for i in range(r):
    x = []
    for j in range(c):
        x.append(int(input(f"Enter element at row {i+1}, column {j+1}: ")))
    A.append(x)
for i in range(r):
    for j in range(c):
        print(A[i][j], end=" ")
    print()'''
def get_matrix(rows, cols, matrix_name):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            element = int(input(f"Enter element at row {i+1}, column {j+1} for matrix {matrix_name}: "))
            row.append(element)
        matrix.append(row)
    return matrix

r = int(input("Enter number of rows: "))
c = int(input("Enter number of columns: "))

print("Enter elements for pradeep the first matrix A:")
A = get_matrix(r, c, 'A')

print("Enter elements for the second matrix B:")
B = get_matrix(r, c, 'B')

result = []
for i in range(r):
    row = []
    for j in range(c):
        row.append(A[i][j] + B[i][j])
    result.append(row)

print("The resulting matrix after addition is:")
for row in result:
    print(" ".join(map(str, row)))
