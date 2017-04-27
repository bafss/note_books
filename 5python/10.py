#coding=utf-8
'''
学以致用，边学边练，在开发中发挥强大的生产力
https://www.python.org/downloads/release/
'''
import sys
#变量
a = 12
print a
print id(a)         #变量a在内存中的编号
print type(a)     #a的类型

b = 12.12
c = b
print id(b)
print id(c)
print type(b)
print type(c)

c = "hello"
print type(b)
print type(c)

del(a)
#print a
#输入输出函数
charset = sys.getfilesystemencoding()
notice = "请输入:".decode('utf-8').encode(charset)
#print notice
str = raw_input(notice)
print type(str)
num = int(str)
print type(num)

print "%s is week %d"%('today',1)
#重定向
logfile = open('./10.py.log','a')
print >> logfile,'error'
logfile.close()
#简单函数
def add(x,y):
    z = x + y
    return z
res = add(3,5)
print res















