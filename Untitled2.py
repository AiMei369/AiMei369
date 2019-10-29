#!/usr/bin/env python
# coding: utf-8

# In[6]:


def crypt(source,key):
    from itertools import cycle
    result=""
    temp=cycle(key)
    for ch in source:
        result=result +chr(ord(ch) ^ ord(next(temp)))
    return result

source="Shandong Institute of Business and Technology"
key="Dong Fuguo"

print("Before Encrypted:"+source)
encrypted=crypt(source,key)
print("After Encrypted:"+encrypted)
decrypted=crypt(encrypted,key)
print("After Decrypted:"+decrypted)


# In[5]:


import string
def check(pwd):
    #密码必须至少包含6个字符
    if not isinstance(pwd,str) or len(pwd)<6:
        return"not suitable for password"
    #密码强度等级与包含字符种类的对应关系
    d={1:"weak",2:"below middle",3:"above middle",4:"strong"}
    #分别用来标记pwd是否含有数字、小写字母、大写字母和指定的标定符号
    r=[False]*4
    for ch in pwd:
        #是否包含数字
        if not r[0] and ch in string.digits:
            r[0]=True
        #是否包含小写字母
        elif not r[1] and ch in string.ascii_lowercase:
            r[1]=True
        #是否包含大写字母
        elif not r[2] and ch in string.asxii_uppercase:
            r[2]=True
        #是否包含指定的标点符号
        elif not r[3] and ch in ",.!;?<>":
            r[3]=True
    #统计包含的字符种类，返回密码强度
    return d.get(r.count(True),"error")
print(check("a2Cd,"))


# In[13]:


from random import choice,randint
import string
import codecs
StringBase="\u7684\u4e00\u4e86\u662f\u6211\u4e0d\u5728\u4eba"
def getEmail():
    suffix=[".com",".org",".net",".cn"]
    characters=string.ascii_letters+string.digits+"_"
    username="".join((choice(characters)for i in range(randint(6,12))))
    domain="".join((choice(characters)for i in range(randint(3,6))))
    return username+"@"+domain+choice(suffix)
def getTelNo():
    return"".join((str(randint(0,9))for i in range(11)))
def getNameOrAddress(flag):
    """flag=1表示返回随机姓名，flag=0表示返回随机地址"""
    if flag==1:
        rangestart,rangeend=2,5
    elif flag==0:
        rangestart,rangeend=10,30
    result="".join((choice(StringBase)for i in range(randint(rangestart,rangeend))))
    return result
def getSex():
    return choice(("男","女"))
def getAge():
    return str(randint(18,100))
def main(filename):
    with codecs.open(filename,"w","utf-8")as fp:
        fp.write("Name,Sex,Age,TelNO,Address,Email\n")
        for i in range(200):
            name=getNameOrAddress(1)
            sex=getSex()
            age=getAge()
            tel=getTelNo()
            address=getNameOrAddress(0)
            email=getEmail()
            line=",".join([name,sex,age,tel,address,email])+"\n"
            fp.write(line)
def output(filename):
    with codecs.open(filename,"r","utf-8")as fp:
        for line in fp:
            line=line.split(",")
            for i in line:
                print(i,end=",")
            print()
if __name__=="__main__":
    filename="information.txt"
    main(filename)
    output(filename)


# In[ ]:




