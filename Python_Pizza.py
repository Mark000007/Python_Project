print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
bill=0
if (size=="S" or size=="s"):
    bill=15
    if(pepperoni=="Y" or pepperoni=="y"):
        bill=bill+2
elif (size=="M" or size=="m"):
    bill=20
    if (pepperoni == "Y" or pepperoni == "y"):
        bill = bill + 3
elif(size=="L" or size=="l"):
    bill=25
    if (pepperoni == "Y" or pepperoni == "y"):
        bill = bill + 3
else:
    print("Wrong input")
#adding for extra cheese
if(extra_cheese=="Y" or extra_cheese=="y"):
    bill=bill+1
#print the total bill
print(f"Your final bill is: ${bill}")