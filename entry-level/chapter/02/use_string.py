name = "my \t name is {name}, I am {year} old"

# capitalize()将字符串的第一个字母变成大写,其他字母变小写。对于 8 位字节编码需要根据本地环境。
print(name.capitalize())
print(name.expandtabs(tabsize=30))
# Python count() 方法用于统计字符串里某个字符出现的次数。可选参数为在字符串搜索的开始与结束位置。
# str.count(sub, start= 0,end=len(string))
print(name.count("a"))

# center() 返回一个原字符串居中,并使用空格填充至长度 width 的新字符串。默认填充字符为空格。
print(name.center(50, "-"))

print(name.endswith("d"))

print(name.format(name="jack", year=13))

print(name.format_map({'name': 'rose', 'year': 13}))

# Python isalnum() 方法检测字符串是否只由字母和数字组成。
print('abc123 !'.isalnum())

# Python isalpha() 方法检测字符串是否只由字母组成。
print('abA'.isalpha())

# Python isdecimal() 方法检查字符串是否只包含十进制字符。这种方法只存在于unicode对象。
# 注意:定义一个十进制字符串，只需要在字符串前添加 'u' 前缀即可。
print('1A'.isdecimal())

# Python isdigit() 方法检测字符串是否只由数字组成。
print('1A'.isdigit())

# 判读是不是一个合法的标识符
print('a 1A'.isidentifier())

# Python isnumeric() 方法检测字符串是否只由数字组成。这种方法是只针对unicode对象。
print('33A'.isnumeric())

# Python istitle() 方法检测字符串中所有的单词拼写首字母是否为大写，且其他字母为小写。
print('My Name Is  '.istitle())

print('My Name Is  '.isprintable())

# 检验是否全部是大写
print('MY  '.isupper())

print('+'.join(['1', '2', '3']))

print(name.ljust(50, '*'))
print(name.rjust(50, '-'))

print("JACK".lower())
print("jack".upper())

# Python lstrip() 方法用于截掉字符串左边的空格或指定字符。
print('\njack'.lstrip())
print('jack\n'.rstrip())
print('    jack\n'.strip())

# Python maketrans() 方法用于创建字符映射的转换表，对于接受两个参数的最简单的调用方式，第一个参数是字符串，表示需要转换的字符，第二个参数也是字符串表示转换的目标。
# 注：两个字符串的长度必须相同，为一一对应的关系。
# Python translate() 方法根据参数table给出的表(包含 256 个字符)转换字符串的字符, 要过滤掉的字符放到 del 参数中。
p = str.maketrans("abcdefli", '123$@456')
print("alex li".translate(p))

p2 = str.maketrans("xxxxxx", "aaaaaa")
print("x1212121".translate(p2))

print('setsunas...'.replace('s', 'S', 3))
print('liu lil'.rfind('l'))
print('1+2+3+4'.split('\n'))
print('1+2\n+3+4'.splitlines())
print('zhang San'.swapcase())
print('Setsuna Setsuna'.title())
print('Pis'.zfill(50))

