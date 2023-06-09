import random

choice = int(input("Rock: 0\nPaper: 1\nScissor: 2\n"))

computer = random.randint(0, 2)

if(computer == 0 and choice == 0):
    print("Tie")
elif(computer == 1 and choice == 1):
    print("Tie")
elif(computer == 2 and choice == 2):
    print("Tie")
elif(computer == 0 and choice == 1):
    print("You Win")
elif(computer == 0 and choice == 2):
    print("You Lose")
elif(computer == 1 and choice == 0):
    print("You Lose")
elif(computer == 1 and choice == 2):
    print("You Win")
elif(computer == 2 and choice == 0):
    print("You Win")
elif(computer == 2 and choice == 1):
    print("You Lose")