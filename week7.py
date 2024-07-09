def read_mat(A, r, c):
    for i in range(r):
        t = []
        for j in range(c):
            val = int(input(f"Enter the A[{i}][{j}] value: "))
            t.append(val)
        A.append(t)

def disp_mat(A):
    for row in A:
        print(row)

def sum_mat(A, B, r, c):
    C = []
    for i in range(r):
        t = []
        for j in range(c):
            val = A[i][j] + B[i][j]
            t.append(val)
        C.append(t)
    return C

mat_A = []
read_mat(mat_A, 3, 2)
print("Matrix A:")
disp_mat(mat_A)

mat_B = []
read_mat(mat_B, 2, 2)
print("Matrix B:")
disp_mat(mat_B)

if len(mat_A) == len(mat_B) and len(mat_A[0]) == len(mat_B[0]):
    mat_C = sum_mat(mat_A, mat_B, len(mat_A), len(mat_A[0]))
    print("Matrix C (A + B):")
    disp_mat(mat_C)
else:
    print("Matrices A and B have different dimensions and cannot be added.")
