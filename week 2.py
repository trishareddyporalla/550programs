
'''rows = 5
for i in range (0,rows):
    for j in range(0,i + 1):
        print(row-i,end=' ')
        print("\r")
        row=int (input("enter number of rows"))
        i=0
        while(i<row):
            j=0
            while(j<i+1):
                print(row-i,end=' ')
                j=j+1;
                i=i+1
                print("\r")
                '''



n=int(input("enter a number"))
temp=n
for i in range (1,n+1):
    for j in range (1,i+1):
        print(temp,end=" ")
    temp=temp-1
    print("\r")