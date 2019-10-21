#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
import requests
import hashlib
import time
import json

key = 'w6%evryhy@mH^J4B'
url = "http://192.168.75.201:8000/panel/api/submitJob"
data = [
    {
        'fastqPath': '/data/data/income', #提交任务前, 请将 19FC40509F_1.fq.gz 和 19FC40509F_2.fq.gz 文件拷贝至此目录下， 任务运行时, fastq文件将会被移动至/data/data/task (详细路径请参阅接口返回数据)
        u'报告编号': '19FC40509',         #请注意 报告编号 与 样本编号 的细微差别
        u'样本编号': '19FC40509F',        # fasq文件命名规则为:  样本编号_1.fq.gz 样本编号_2.fq.gz
        u'OEM编号': '',                   #可为空
        u'报告panel': '10gene',           #['10gene', '15gene', 'brca', 'brcaDrug',]
        u'计算平台': 'compute',            #['compute',]
        u'测序平台': 'Illumina',          #['Illumina',]
        u'渠道': 'FC',                    #['FC',]
        u'姓名': u'测试',                 #可为空
        u'样本种类': u'肿瘤组织',         #[u'肿瘤组织', u'血液',]
        u'性别': u'男',                   #[u'男', u'女']
        u'年龄': '60',                    #可为空
        u'采样日期': '01/11/2017',        #可为空
        u'接收日期': '01/10/2018',        #可为空
        u'临床诊断': u'右肺癌',           #可为空
        u'病理诊断类型': u'肺腺癌',       #可为空
        u'病理分期': u'测试',             #可为空
        u'用药治疗史': u'测试',           #可为空
        u'肿瘤家族史': u'测试',           #可为空
        u'吸烟史': u'吸烟30年，戒烟6年',  #可为空
        u'住院号': u'测试',               #可为空
        u'病理号': u'测试',               #可为空
        u'送检科室': u'测试',             #可为空
        u'送检医生': u'测试',             #可为空
        u'主要设备': '7',                 #[1 - Ion Torrent PGM、2 - HiSeq 2500、3 - NextSeq CN500、4 - MiSeq、5 - HiSeq 3000、6 - HiSeq X Ten、7 - MiniSeq]
        u'癌种类型': u'肺癌',             #[u"未知", u"肝胆肿瘤", u"鼻咽癌", u"恶性胸膜间皮瘤", u"宫颈癌", u"卵巢癌", u"滋养细胞层肿瘤", u"子宫内膜癌", u"子宫肉瘤", u"胃癌", u"乳腺癌", u"肾细胞癌", u"结直肠癌", u"食管癌", u"前列腺癌", u"睾丸癌", u"膀胱癌", u"骨和软组织肿瘤", u"原发不明癌", u"胰腺癌", u"头颈部肿瘤（非鼻咽癌）", u"脑胶质瘤", u"黑色素瘤", u"肺癌", u"小细胞肺癌", u"非小细胞肺癌", u"白血病", u"淋巴瘤"]
    },
    { 'fastqPath': '/data/data/income', u'报告编号': 'test', u'样本编号': 'test', u'OEM编号': '', u'报告panel': '15gene', u'计算平台': 'compute', u'测序平台': 'Illumina', u'渠道': 'FC', u'姓名': u'测试', u'样本种类': u'肿瘤组织', u'性别': u'男', u'年龄': '60', u'采样日期': '01/11/2017', u'接收日期': '01/10/2018', u'临床诊断': u'右肺癌', u'病理诊断类型': u'肺腺癌', u'病理分期': u'测试', u'用药治疗史': u'测试', u'肿瘤家族史': u'测试', u'吸烟史': u'吸烟30年，戒烟6年', u'住院号': u'测试', u'病理号': u'测试', u'送检科室': u'测试', u'送检医生': u'测试', u'主要设备': '7', u'癌种类型': u'肺癌', },
]

authTime = time.time()
authKeyTime = "%s|%s"%(key, authTime)
m = hashlib.md5()
m.update(str(authKeyTime).encode())
authKey = m.hexdigest()
headers = {'authKey': authKey, 'authTime': str(authTime)}

result = json.loads(requests.post(url=url, data=json.dumps(data), headers=headers).text)
print (str(result).decode('unicode_escape'))

#示例：
#异常返回 {u'status': u'error', u'msg': u'Invalid API key', u'result': {}}
#正常返回 {u'status': u'success', u'msg': u'', u'result': {u'test': [u'/data/data/task/test_5d9c00c3921e18cce8e23237', u'test_测试_肺癌靶向用药全面检测_血检_肿瘤组织.docx'], u'19FC40509F': [u'/data/data/task/19FC40509F_5d9c00c3921e18cce8e23236', u'19FC40509_测试_肺癌靶向用药标准检测_血检_肿瘤组织.docx']}}
#u'result'键值:
#             包含 该样本的文件目录,  例如 /data/data/task/test_5d9c00c3921e18cce8e23237
#             包含 该样本的word文件名 例如 test_测试_肺癌靶向用药全面检测_血检_肿瘤组织.docx

#当 /data/data/task/'/data/data/task/19FC40509F_5d98501134a089177624c627/analysis/docx/ 目录中 唯一 以docx为扩展名的文件, 即 word文件 存在, 标志着 此样本 分析完毕



proof=int(input("请输入述职"))
if proof<20:
    print("不构成醉驾")
else:
    if proof<80:
        print("jiujia")
    else:
        print("zuijia")

#pass
s=input("请输入一个整数")
s=int(s)

if s>5:
    print("s>5")
elif s < 5:
    pass
else:
    print("=5")

test=99
#assert 5<test<55


def func(input):
    assert isinstance(input,list)
    if len(input)==1:
        pass
    elif len(input)==2:
        print("=2")
        pass
    else:
        pass

slist=(1,2)
#func(slist)

num=1
while num<100:
    print("num is",num)
    num+=1
print("end")

a_tuple=('1','2','3','4')
i=0
while i<len(a_tuple):
    print(a_tuple[i])
    i+=1

src_list=[12, 45, 34,13, 100, 24, 56, 74, 109]
a_list=[]
b_list =[]
c_list=[]
i=0
while i<len(src_list):
    if src_list[i]%3==0:
        a_list.append(src_list[i])
    elif src_list[i]%3==1:
        b_list.append(src_list[i])
    elif src_list[i]%3==2:
        c_list.append(src_list[i])
    else:
        pass
    i+=1

print("alist:",a_list)
print("blist",b_list)
print("clist",c_list)


name ="zhagnsan"
for A in name:
    print(A)


result=0
for v in range(1,100,2):
    result+=v
print(result)

a_tupl=(1,'fa',-1)
for ac in a_tupl:
    if isinstance(ac,str):
        print(ac)
'''


my_dict={'a':1,'b':2,'c':3}

for key1,valu1 in my_dict.items():
    print("key1 and value is:",key1,valu1)

for key in my_dict.keys():
    print(key)

for value in my_dict.values():
    print(value)

src_list = [12, 45, 3.4, 12, 'fkit', 45, 3.4, 'fkit', 45, 3.4]
#statics=[]
statics={}

for val in src_list:
    if val in statics:
        statics[val]+=1
    else:
        statics[val]=1

for ele,count in statics.items():
    print(ele,count)


my_dic1={1:2,3:4}
for a,b in my_dic1.items():
    print(a,b)

aaa=1
if aaa in my_dic1:#查看的是键是否在字典中
    print("true")


for i in range(0,10):
    print("i is:",i)
    if i >3:
        break

exit_flag=False
for i in range(0,5):
    for j in range(0,4):
        print("i,j is:",i,j)
        if j==1:
            exit_flag=True
            break #跳出内层循环 不跳出外层循环
    if exit_flag==True:
        break


for va in range(0,3):

    if  va==1:
        continue
    print("va is",va)

a_range=range(10)
lis1=[x*x for x in a_range if x%2==0]
#print(lis1)

d_list=[(x,y) for x in range(1,10) for y in range(1,3)]
d_list=[]
#print(d_list)

for x in range(4):
    for y in range(3):
        d_list.append((x,y))

print(d_list)

a=(x for x in range(1,10))
print(tuple(a))

dictlist=['woshizhongw','aaa']
a_dict={key:len(key) for key in dictlist}
print(a_dict)

olddict={'cyuyan':3,'c++':4}
newdict={k:v for v,k in olddict.items()}
print(newdict)

set1={x**2 for x in range(7)}
print(set1)

a=['a','b','c']
b=[1,2,3]
d=[0.1,0.2]
c=[x for x in zip(a,b)]
e=[x for x in zip(a,d)]
print(c)
print(e)

f=[x for x in zip(a,b,d)]
print(f)


a=range(10)
b=reversed(a)
#print(b) 得加list
print(list(b))

b=['a','b','c']
b=reversed(b)
print(list(b))

str1='abcdefg'
#str2=reversed(str1)不能这样的
str2=[x for x in reversed(str1)]
print(str2)

a=[1,8,3,9,7]
b=sorted(a,reverse=True)#反向排序
print(b)

a=['aaaa','da','caa','zaaaa','y']
b=sorted(a,key=len)#根据长度

my_list = ['fkit', 'crazyit', 'Charlie', 'fox', 'Emily']
for s in sorted(my_list,key=len):
    print(s)
