import sys

print(sys.getdefaultencoding())

words = "狗蛋,谢谢"

words_gbk = words.encode("gbk")

print(words_gbk)
print(words.encode())

gbk_to_utf8 = words_gbk.decode("gbk").encode("utf-8")
print("utf-8", gbk_to_utf8)
