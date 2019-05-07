secret_number = 7
print("Enter a number!")
user_number = input()
num = int(user_number)
if secret_number == num:
    print("You win!")
elif secret_number == num - 1 or secret_number == num + 1:
    print("So close!")
else:
    print("Try again!")


