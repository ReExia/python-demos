age = 33

count = 0
while count < 3:
    guess_age = int(input("guess age:"))
    if age == guess_age:
        print("yeah, you got it.")
        break
    elif guess_age > age:
        print("higher....,try again.")
    else:
        print("lower....,try again.")
    count += 1
else:
    print("you have tried too many times...fuck off")
