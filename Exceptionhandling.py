
try:
    #a=int(input("enter the value:"))
    #b=int (input("enter the b value:"))
    #c=a/b
    #print("the value of c is",c)(
    x=[1,2,3,4]
    print(x[5])

except NameError:
    print("b  value is not mentioned")
except ZeroDivisionError:
    print("Arithmatic Exception")
except ValueError:
    print("Array Index Out Of Bound")
except KeyError:
    print("Key Error")
except IOError:
    print("Input Output Error")
print("After Exception")

