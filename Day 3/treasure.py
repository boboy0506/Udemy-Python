print("Welcome to Treasure Island.\nYour mission is to find the treasure.")

direction = input("Left or Right?")

if (direction == "left"):
    swim = input("Swim or Wait?")
    if(swim == "wait"):
        door = input("Which Door? Yello, Red, Blue")
        if(door == "yellow"):
            print("You Win!")
        elif(door == "red"):
            print("Burned by fire.\nGame Over.")
        elif(door == "blue"):
            print("Eaten by Beast\nGame Over.")
        else:
            print("Game Over.")
    else:
        print("Attacked by trout.\nGame Over.")
else:
    print("You fall into a hole.\nGame Over.")