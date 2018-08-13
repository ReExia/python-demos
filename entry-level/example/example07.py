'''
文件io
'''

# 写文件
with open("test.txt", "wt", encoding="utf-8") as out_file:
    out_file.write("该文本会写入到文件中\n")

with open("test.txt", "rt") as in_file:
    text = in_file.read()

print(text)
