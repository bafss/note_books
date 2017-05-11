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
print("hello{_name},your age:{_age}".format(_age = 26,_name = 'llz'))#找不到返回-1
print("2".isalnum())#判断是否含字母或数字
print("45a".isalpha())#判断是否为字母
print("45".isdigit())#判断是否为数字
print("space:","\t".isspace())#判断是全部为空格
print("The School".istitle())#判断是否为标题
print("_".join(['l','l','z']))#连接列表为字符串
print("llz".ljust(10,'*'))#右边补*
print(" l lz ".strip())#去空格
print(" l lz ".partition(" "))#分割为3部分
print(" l lz ".split(" "))#分割
print(" l lz ".split(" ",1))#找到第一个空格分割为2部分
print(" l lz ".replace(" ","x",2))#从左往右替换2个
print("the school".title())#变成标题格式
print("the school"[0])#
print(len("the school"))#
str = "school"
for v in str:
	print(v)
#list列表
arr = ['hello','china']
for v in arr:
	print(v)

print(arr[1:len(arr)])#切片
arr.append('by')
print(arr)#追加
print(arr.count('by'))#
arr.extend(('xjw','wh'))
print(arr)
print(arr.index('xjw'))
arr.insert(4,'myq')
print(arr)
last = arr.pop()
print(last)
arr.remove('myq')#只移除一个，全部要循环移除
print(arr)
arr.reverse()
print(arr)
arr.sort()
print(arr)
print('hello' in arr)
print('hello' not in arr)
#元祖

#字典