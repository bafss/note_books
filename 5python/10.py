#coding=utf-8
'''
学以致用，边学边练，在开发中发挥强大的生产力
下载python解释器： https://www.python.org/downloads/release/
'''
'''
import sys
print("hello world")
'''
#注释，增加程序可读性
'''
多行注释
'''
'''
变量以及类型
    变量是存储数据的
    变量类型  type(变量)
    数字：int（有符号整型）、long（长整型）、float（浮点型）、complex（复数）
    布尔类型：True、False
    字符串
    列表list
    元祖tuple
    字典dictionary
运算符
    算术运算符：//    取商的整数部分
    **  幂运算2的3次方
'''
"""
num = '12'
num2 = "12a"
print(num.isdigit())
print(num2.isdigit())
"""
"""
a = 12
b = 5
c = a+b
print ( c)
id_a = id(a) 
print  (id_a)       #变量a在内存中的编号
type_a = type(a) 
print  (type_a)   #a的类型

b = 12.12
c = b
id_b = id(b)
id_c = id(c)
print (id_b)
print (id_c)
type_b = type(b)
type_c = type(c)
print (type_b)
print (type_c) 

c = "hello"
type_b = type(b)
type_c = type(c)
print (type_b)
print (type_c) 

del(a)
#print a
"""
#byte字节类型。二进制
"""
str  = '李利钊'
print(str)
print(str.encode(encoding='utf8'))
print(str.encode(encoding='utf8').decode(encoding='utf8'))
"""
#列表
"""
names = ['沙瑞金','侯亮平','李达康']
print(names[1:3])   #切片
print(names[-1])   #切片
print(names[-2:])   #切片
names.append('祁同伟')
print(names)
names.insert(3,'易学习')
print(names)
names[4] = '高育良'
print(names)
names.remove('高育良')
print(names)
del names[1]
print(names)
names.pop(-2)#默认最后一个
print(names)
print(names.index('易学习'))
names.append('沙瑞金')
print(names.count('沙瑞金'))
print(names)
names.sort()
print(names)
names2 = ['林华华','陆亦可']
names.extend(names2)
print(names)
names.append(['蔡成功','丁义珍'])
name3 = names.copy()#浅复制，只会复制第一层，二层以上引用地址
print(name3)
name3[2] = '李达康'
name3[5][0] = '欧阳菁'
print(names)
print(name3)
import copy#导入copy模块
name3 = copy.deepcopy(names)#全复制
print(name3)
name3[2] = '李达康'
name3[5][0] = '高小琴'
print(names)
print(name3)
for name in names:
    print (name)
"""
#元祖.就是列表，只能看不能改。只有count和index方法
"""
names4 = ('孙悟空','猪八戒')
print(names4[0])
print(names4.count("猪八戒"))
print(names4.index('猪八戒'))
print(len(names4))
for key,value in enumerate(names4):
    print(key,value)
"""
"""

a = 5
b = 3
max = a if a > b else b#三元运算符
min = b if a > b else a
print("max:",max)
print("min:",min)
"""
#用户输入  输出函数
#字符在计算机存储为0和1，ASCII码1个字节，gbk汉字为2个字节，utf-8汉字3个字节，是对unicode万国码（都是2个字节）的优化和压缩
'''
notice = "请输入:"
#print notice
str = input(notice)
type_str = type(str)
print (type_str)
num = int(str)
type_num = type(num)
print (type_num)
'''
"""
print ("%s is week %d"%('today',1)) 
print('''

多行
输出
''')

name = 'llz'
age = 26
print(
'''
{_name}
{_age}
'''.format(
        _name = name,
        _age=age
    )
)
"""
#流程控制
'''
import getpass
password = getpass.getpass("密码：")
print(password)
_password = '123'
if password == _password and 1:
    print("登录成功")
else:
    print("登录失败")
'''
'''
true_age = 26
count = 0

while count < 3:
    guess_age = input('猜猜我多大了')
    guess_age  =int(guess_age)
    if true_age == guess_age :
        print('猜对了')
        break
    elif true_age > guess_age :
        print('往大了猜')
    else :
        print('往小了猜')
    count += 1
#else只在循环正常循环完时进入，break循环不进入
else:
    print("已经猜3次了，不能再猜了")
    # print (count)
for i in range(0,3,1) :
    guess_age = input('for猜猜我多大了')
    guess_age  =int(guess_age)
    if true_age == guess_age :
        print('猜对了')
        break       #continue结束本次循环，继续下一次循环
    elif true_age > guess_age :
        print('往大了猜')
    else :
        print('往小了猜')
    count += 1
else:
    print("已经猜3次了，不能再猜了")
for i in range(0,10,3):
    print(i)
'''
'''
模块
'''
"""
import sys
print(sys.argv)#运行文件的参数
print(sys.path)#打印当前目录和环境变量，从这些位置找库文件
import os
cmd_res = os.popen('dir')#cmd命令执行结果的地址
print(cmd_res)
cmd_res = cmd_res.read()
print(cmd_res)
# os.makedirs('par_dir/sub_dir')#递归创建子目录
#os.mkdir('par_dir1')
"""
#简单函数
"""
def add(x,y):
    z = x + y
    return z
res = add(3,5)
print (res)
"""
#字符串函数

name = 'llz'
print(name.capitalize())#首字母大写
print(name.count('l'))#字母个数
print(name.center(10,'-'))#打印10个字符，字符串放中间
print(name.endswith('z'))#是否以z结尾
space = "a\tc"
print(space.expandtabs(10))#把制表符替换为几个空格












