class person:
    name = ''
    sex = ''
    age = -1

    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age

    def speak(self):
        print("%s 说: 我 %d 岁。" % (self.name, self.age))


p = person("zhangsan",12,33)
p.speak()

