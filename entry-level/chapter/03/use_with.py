import sys

with open("./test.txt", "r", encoding="utf-8") as f, \
        open("./test2.txt", "r", encoding="utf-8") as f2:
    for line in f:
        print(line)
    for line2 in f2:
        print(line2)
