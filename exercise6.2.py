distance = 0 
energy = int(10)
answer = ""
while energy >= 3:
    while answer != "go home":
        print("Would you like to Walk, Run or Go Home?")
        answer = input().lower()
        if energy <= 2:
            print("You rock! Please rest and eat now!")
            break
        if answer == "walk":
            distance += 1
            energy += 1
            print("Distance from home is {}km and your energy level is {}".format(distance, energy))
        elif answer == "run":
            distance += 5
            energy -= 3
            print("Distance from home is {}km and your energy level is {}.".format(distance, energy))
        elif answer == "go home":
            print("Tracker has been turned off.")   
        else:
            print("Not Found :(\nPlease try again!") 
if energy <= 0:
    energy = 0