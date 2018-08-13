age = 33
for i in range(3):
    guess_age = int(input("guess age:"))
    if guess_age == age:
        print("yes, you got it")
        break
    elif guess_age > age:
        print("higher...,try again")
    else:
        print("lower...,try again")
else:
    print("you have tried too many times..fuck off")
