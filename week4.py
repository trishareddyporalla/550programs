
#4.3(i)
'''def commas(str):
    x=str.replace('',',')[1:-1]
    return x
    print(word)
print(repr(commas("Apple")))'''
#"repr" ---converts object to string

#4.3(ii)
'''def remove_word(str,word):
    str2=str.replace(word,'')
    return str2
str3="hello gd mrng hi hello good"
str4=remove_word(str3,"hello")
print(str4)'''

#4.3(iii)
#ord is a function to convert num to asscii value
#chr is a function to convert asscii value to num
'''print(ord('A'))
print(ord('*'))
print(ord('+'))
print(ord('!'))
print(ord('~'))'''

#4.3(iv)
def convert(str):
    ch=list(str)
    for i in range(len(str)):
        if(i==0 & ch[i]!=''):
            if(ch[i]>='a' & ch[i]<='2'):
                ch[i]=chr(ord(ch[i]-ord('a')+ord('A')))

