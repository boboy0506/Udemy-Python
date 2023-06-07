name1 = input("Enter your name: ")
name2 = input("Enter their name: ")

combined_name = name1 + name2
low = combined_name.lower()

t = low.count("t")
r = low.count("r")
u = low.count("u")
e = low.count("e")

true = t + r + u + e 

l = low.count("l")
o = low.count("o")
v = low.count("v")
e = low.count("e")

love = l + o + v + e

scoreStr = str(true) + str(love)

score = int(scoreStr) 

if(score <10 or score >90):
    print(f"Your score is {score}, you go together like coke and mentos")
elif(score >40 and score <50):
    print(f"Your score is {score}, you are alright together")
else:
    print(f"Your score is {score}")

