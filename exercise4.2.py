print("Enter your age!")
age = input()
if int(age) < 105:
    difference = int(age) - 24
    if difference < 0:
        print("You are {} years apart in age than me.".format(difference))
    elif difference > 0:
        print("You are {} years apart in age than me.".format(difference))
    else:
        print("We are the same age!")
else:
    print("I'm not sure I believe you.")