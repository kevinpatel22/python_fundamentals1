# 1. Solution
#Amount of tip in dollars for any size of a meal
print ("Would you like to give tip?")
answer = input()
if answer == "yes" or "y":
    print("How generous are you? (Must be in %)")
    tip_percent = input()
    tipvalue = int(tip_percent)
    tip_amount = (55 * tipvalue)/100
    print("Your tip amount is ${}".format(tip_amount))

# 2. Solution
value = str(10)
print("Hi" + value)

# 3. Solution
print("The answer is {}".format(45628*7839))

# 4. Solution
print ((10 < 20 and 30 < 20) or (10 != 11))