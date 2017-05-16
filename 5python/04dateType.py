#数字
#id(对象)	对象的内存地址
n1 = 123
n2 = 123
print(id(n1))
print(id(n2))
#字符串
str = "hello"

print('h' in str)
print('h' not in str)
str = "你很nice"
for v in str:
	print(v)
	b_16 = bytes(v,'utf-8')#字节类型,16进制
	print(b_16)
	print(b_16.decode())
	for b_10 in b_16:
		print(b_10,bin(b_10))#bin()二进制表示

temp = "small\tend"
print(isinstance(temp,int))
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
for k,v in enumerate(arr,2):#2起始序号
	print(k,v)
	print(arr[k-2])
for v in arr:
	print(v)
rangelist = range(0,10,2)
print(rangelist)
rangelist = range(10,1,-2)
print(rangelist)
for i in rangelist:
	print(i)
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
del(arr[2])
print(arr)
del(arr[1:4])
print(arr)
print('hello' in arr)
print('hello' not in arr)
#元祖

#字典
stu = {
	'name':'llz',
	'age':26
}
print(stu['age'])
for key,value in stu.items():
	print(key,value)
for key in stu:
	print(stu[key])
print(stu.keys())
print(stu.values())
print(stu.items())
stu.clear()
print(stu)
default = stu.get('gender','male')
print(default)
insert = {
	'hobby':'nv'
}
stu = {'name':'llz'}
stu.update(insert)
print(stu)
del(stu['hobby'])
print(stu)
stu['hobby'] = 'nv'
print(stu)
old_dic = {
	'#1':11,
	'#2':22,
	'#3':100,
}
new_dic = {
	'#1':33,
	'#4':22,
	'#7':100,
}
#要求：新旧都有删除旧的，新中没有，删除旧的，新有旧没有，添加
print('c' in ['c'])
new_keys = new_dic.keys()
old_keys = old_dic.keys()
old_too_new_keys = set(old_keys) & set(new_keys)
print(old_too_new_keys)
for i in old_too_new_keys:
	old_dic[i] = new_dic[i]
old_del_keys = set(old_keys) - set(new_keys)
print(old_del_keys)
for i in old_del_keys:
	del(old_dic[i])
old_add_keys = set(new_keys) - set(old_keys)
for i in old_add_keys:
	old_dic[i] = new_dic[i]
print(old_dic)
copy1 = [0,1,[1,2,[3,[5]]]]
copy2 = copy1#只是引用地址，相当于php的引用赋值
print(copy1,id(copy1))
print(copy2,id(copy2))
copy2[1] = 8
print(copy1)
print(copy1)
import copy
copy3 = copy.deepcopy(copy1)
print(copy3)
copy3[1] = 9
print(copy1)
print(copy3)
#集合，类似数学的集合
se = set()
se.add(5)
print(se)
s1 = {1,2,3,5}
s2 = {1,5,6}
print(s1 - s2)
print(s2 - s1)
print(s1 & s2)