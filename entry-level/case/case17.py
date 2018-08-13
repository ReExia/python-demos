# 函数

'''
def printHello():
    print("hello",end="")


def printWorld():
    print("world",end="")


def printAll():
    printHello()
    printWorld()


def getNumber():
    return 133

printAll()
a = getNumber()
print()
print(a)
'''

'''
可更改(mutable)与不可更改(immutable)对象
在 python 中，strings, tuples, 和 numbers 是不可更改的对象，而 list,dict 等则是可以修改的对象。

不可变类型：变量赋值 a=5 后再赋值 a=10，这里实际是新生成一个 int 值对象 10，再让 a 指向它，而 5 被丢弃，不是改变a的值，相当于新生成了a。

可变类型：变量赋值 la=[1,2,3,4] 后再赋值 la[2]=5 则是将 list la 的第三个元素值更改，本身la没有动，只是其内部的一部分值被修改了。
'''

'''
def ChangeInt(a):
    a = 10


def getInt(a):
    a = 10
    return a


b = 2
ChangeInt(b)
print(b)  # 结果是 2
print("-----------------")
c = getInt(b)
print(b)
print(c)

x = int(2.9)  # 内建作用域

g_count = 0  # 全局作用域
'''

'''
global 和 nonlocal关键字

global : 关键字用来在函数或其他局部作用域中使用全局变量
nonlocal : nonlocal关键字用来在函数或其他作用域中使用外层(非全局)变量。
'''
'''
total = 0  # 这是一个全局变量
# 可写函数说明
def sum(arg1, arg2):
    # 返回2个参数的和."
    # global total
    total = arg1 + arg2  # total在这里是局部变量.
    print("函数内是局部变量 : ", total)
    return total
# 调用sum函数
sum(10, 20)
print("函数外是全局变量 : ", total)
'''
def outer():
    num = 10
    def inner():
        nonlocal num   # nonlocal关键字声明
        num = 100
        print(num)
    inner()
    print(num)
outer()



'''
def outer():
    o_count = 1  # 闭包函数外的函数中
    print(o_count);
    def inner():
        i_count = 2  # 局部作用域
        print(o_count)

outer()
'''
