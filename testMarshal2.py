import marshal
fp=open("Marshal2.txt","rb")
data=marshal.load(fp)
exec(data)