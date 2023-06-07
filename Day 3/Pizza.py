print("SIZE\nSmall:  $15\nMedium: $20\nLarge:  $25\n")

size = input("Size: ")
bill = 0

if(size == "s"):
    bill+= 15
    pepperoni = input("Add pepperoni for $2? Y/N: ")
    if(pepperoni == "y"):
        bill+=2
    cheese = input("Add cheese for $1 Y/N: ")
    if(cheese == "y"):
        bill+= 1
elif(size == "m"):
    bill+= 20
    pepperoni = input("Add pepperoni for $3? Y/N: ")
    if(pepperoni == "y"):
        bill+=3
    cheese = input("Add cheese for $1 Y/N: ")
    if(cheese == "y"):
        bill+= 1
elif(size == "l"):
    bill+= 25
    pepperoni = input("Add pepperoni for $3? Y/N: ")
    if(pepperoni == "y"):
        bill+=3
    cheese = input("Add cheese for $1 Y/N: ")
    if(cheese == "y"):
        bill+= 1

print(f"Your total bill is {bill}")


