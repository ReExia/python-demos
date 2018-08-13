# 行与缩进

# value = ""
value = 1

if value:
    print(True)
else:
    print(False)

# 缩进不一致，会导致运行错误
if True:
    print("Answer")
    print("True")
else:
    print("Answer")
