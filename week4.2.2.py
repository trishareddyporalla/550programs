'''
fp = open("word.txt", "w")
if fp:
    print("successfuly opened")
    fp.write("i")
    fp.write("a")
    fp.write(" ")
    fp.close()
'''
# 4.2.3
def invert_content(dic):
    invert_dic = {}
    for k, v in dic.items():
        invert_dic[v] = k
    return invert_dic

n = int(input("Enter no of values: "))
dic = {}
for i in range(n):
    key = input("Enter key: ")
    value = input("Enter value: ")
    dic[key] = value

print("Original dictionary:", dic)

print("After inversion:")
invert_dic = {}
invert_dic = {v: k for k, v in dic.items()}
print(invert_dic)



