'''
5
4 4
3 3 3
2 2 2 2
1 1 1 1 1

'''
rows = 5
for i in range(0, rows):
    #nested loop for each column
    for j in range(0, i + 1):
        # print star
        print(rows - i, end=' ')
    # new line after each row
    print("\r")
rows = int(input("Enter the number of rows: "))

for i in range(0, rows):
    # nested loop for each column
    for j in range(0, i + 1):
        # print number
        print(rows - i, end=' ')
    # new line after each row
    print("\r")

