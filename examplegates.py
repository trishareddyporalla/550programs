def AND(a, b):
    return a == 1 and b == 1

def OR(a, b):
    return a == 1 or b == 1

def XOR(a, b):
    return (a == 1) != (b == 1)

print("A=True|B=True|A AND B=", AND(1, 1), "|A OR B=", OR(1, 1), "|A XOR B=", XOR(1, 1))
print("A=True|B=False|A AND B=", AND(1, 0), "|A OR B=", OR(1, 0), "|A XOR B=", XOR(1, 0))
print("A=False|B=True|A AND B=", AND(0, 1), "|A OR B=", OR(0, 1), "|A XOR B=", XOR(0, 1))
print("A=False|B=False|A AND B=", AND(0, 0), "|A OR B=", OR(0, 0), "|A XOR B=", XOR(0, 0))
