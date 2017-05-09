# -*- coding:utf-8 -*-

str = "你好"
print(str)


str = str.encode('utf-8')
print(str)
str = str.decode('utf-8')
print(str)
str = str.encode('gbk')
print(str)