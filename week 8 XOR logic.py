def XOR(a, b):
    if a!=b :
        return True
    else:
        return False

print("A=True|B=True|A AND B=True", XOR(1, 1))
print("A=True|B=False|A AND B=False", XOR(1, 0))
print("A=False|B=True|A AND B=False", XOR(0, 1))
print("A=False|B=False|A AND B=False", XOR(0, 0))