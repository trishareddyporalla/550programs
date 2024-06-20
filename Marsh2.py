import marshal
src ='''
def factorial(n):
    if n==1 or n==0:
        return 1
    else:
        return n*factorial(n-1)
n=int(input())
print(factorial)


'''
code=compile(src,"src","exec")
fp=open("Marshal2.txt","wb")
marshal.dump(code,fp)
fp.close()