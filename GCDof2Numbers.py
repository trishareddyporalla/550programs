def gcd(a,b):
 if(b==0):
     return a
 else:
     return gcd(b,a%b)
a=int(input("Enter the first number"))
b=int(input("Enter the second number"))
if(a>b):
    temp=a
    a=b
    b=temp
print('gcd of given numbers1',gcd(a,b))