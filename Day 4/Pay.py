import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

namesindex = len(names)

random_choices = random.randint(0, namesindex -1)
payer = names[random_choices]

print(payer)