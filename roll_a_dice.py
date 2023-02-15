import random

response = "yes"
while response == "yes":
    num = random.randint(1,6)
    response = input("Do you wish to roll a die(yes or no) ")
    if num == 1:
        print("[--0--]")
        print("[-----]")
        print("[-----]")
        print("[-----]")
        print("[-----]")
        print("[-----]") 
    if num == 2:
        print("[--0--]")
        print("[--0--]")
        print("[-----]")
        print("[-----]")
        print("[-----]")
        print("[-----]") 
    if num == 3:
        print("[--0--]")
        print("[--0--]")
        print("[--0--]")
        print("[-----]")
        print("[-----]")   
    if num == 4:
        print("[--0--]")
        print("[--0--]")
        print("[--0--]")
        print("[--0--]")
        print("[-----]")
        print("[-----]") 
    if num == 5:
        print("[--0--]")
        print("[--0--]")
        print("[--0--]")
        print("[--0--]")
        print("[--0--]")
        print("[-----]") 
    if num == 6:
        print("[--0--]")
        print("[--0--]")
        print("[--0--]")
        print("[--0--]")
        print("[--0--]") 
        print("[--0--]") 
    print()