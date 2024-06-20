def OR(a, b):
    if a==1 or b==1 :
        return True
    else:
        return False

print("A=True|B=True|A AND B=True", OR(1, 1))
print("A=True|B=False|A AND B=False", OR(1, 0))
print("A=False|B=True|A AND B=False", OR(0, 1))
print("A=False|B=False|A AND B=False", OR(0, 0))