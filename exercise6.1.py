distance = 0 
answer = ""
while answer != "go home":
    print("Would you like to Walk, Run or Go Home?")
    answer = input().lower()
    if answer == "walk":
        distance += 1
        print("Distance from home is {}km.".format(distance))
    elif answer == "run":
        distance += 5
        print("Distance from home is {}km.".format(distance))
    elif answer == "go home":
        (print("Tracker has been turned off."))
    else:
        print("Not Found :(\nPlease try again!")  
