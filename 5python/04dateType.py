#数字

#字符串
str = "hello"
print('h' in str)
print('h' not in str)

temp = "small\tend"
print(type(temp))
print(temp.upper())
print(temp.upper().lower())
print(temp.capitalize())#首字母大写
print(temp.center(20,'-'))#内容居中
print(temp.count('sm',0,4))#从0到4查找出现的次数
print(temp.endswith('m',0,2))#从0到2（不含）判断是否以m结尾
print(temp.expandtabs(4))#将制表符替换为4个空格
print(temp.find('s'))#找不到返回-1
print("hello{_name},your age:{_age}".format(_name = 'llz',_age = 26))#找不到返回-1
#列表
arr = ['hello','china']
print('hello' in arr)
print('hello' not in arr)
#元祖

#字典