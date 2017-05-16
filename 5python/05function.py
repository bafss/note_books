def email(p):
	import smtplib
	from email.mime.text import MIMEText
	from email.utils import formataddr
	ret = True
	try:
		msg = MIMEText('邮件内容','plain','utf-8')
		msg['From'] = formataddr(['武沛齐','m15701560565@126.com'])
		msg['To'] = formataddr(['走人','125917415@qq.com'])
		msg['Subject'] = "主题"

		server = smtplib.SMTP('smtp.126.com',25)
		server.login('m15701560565@126.com','xmxxmx19901003')
		server.sendmail('m15701560565@126.com',[p,],msg.as_string())
		server.quit()
	except:
		ret = False
	return ret

# ret = email('1259174175@qq.com')
# print(ret)


# 函数传参（列表、字典、集合）传的是引用。引用传值
def f(dic):
	print(dic,type(dic))

f({'k1':1})


#全局变量在函数内外都有效，局部变量。函数内可以使用全局变量，但要修改，就要global
#函数内变量一旦被赋值，则函数内变量指向新的值，函数外的变量不受影响
NAME = 'llz'
def f1():
	NAME = 'XMX'
	print(NAME)

def f2():
	global NAME
	NAME = 'XMX'
	print(NAME)
print(NAME)
f1()
print(NAME)
f2()
print(NAME)
