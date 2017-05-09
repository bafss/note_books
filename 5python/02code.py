# -*- coding:utf-8 -*-
#ascii码、万国码（unicode最少两个字节）、utf-8
# utf-8和gbk不能直接互转，只能通过unicode
# 文件中的bytes编码为utf-8，计算机内存中统一使用unicode
str = "你好"
print(str)
str = str.encode('utf-8')#自动的把字符解码码为unicode，编码为utf-8
print(str)
#解码时指定原来的编码
str = str.decode('utf-8')
print(str)
str = str.encode('gbk')
print(str)