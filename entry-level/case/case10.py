# 字符串

'''
var1 = 'Hello World!'
var2 = "setsuna"

print("var1[0]: ", var1[0])
print("var2[1:5]: ", var2[1:5])
'''


# 字符串格式化

print ("我叫 %s 今年 %d 岁!" % ('小明', 10))

errHTML = '''
<HTML><HEAD><TITLE>
Friends CGI Demo</TITLE></HEAD>
<BODY><H3>ERROR</H3>
<B>%s</B><P>
<FORM><INPUT TYPE=button VALUE=Back
ONCLICK="window.history.back()"></FORM>
</BODY></HTML>
'''
print(errHTML)