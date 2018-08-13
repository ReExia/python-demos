name = input("name:")
age = int(input("age:"))
sex = input("sex:")

# type
# print(type(name), type(str(age)), type(sex))
# print(type(name), type(age), type(sex))

# format
info = '''
------------------info of %s-----------------
Name : %s
age : %d
sex : %s
''' % (name, name, age, sex)

# print(info)

info2 = '''
---------------------info of {_name}------------------------
Name :{_name}
Age : {_age}
Sex : {_sex}
'''.format(_name=name,
           _age=age,
           _sex=sex)
# print(info2)

info3 = '''
-------------------------info of {0}------------------------------------
Name : {0}
Age : {1}
Sex : {2}
'''.format(name, age, sex)

print(info3)
