# 多行语句

item_one = "1"
item_two = "2"
item_three = "3"

total = item_one + \
        item_two + \
        item_three

print(total)

# 在 [], {}, 或 () 中的多行语句，不需要使用反斜杠(\)，例如：
total2 = [
    item_one,
    item_two,
]
print(total2)
