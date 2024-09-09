rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = ''' 
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
y=input("Enter y to play\n")
while(y=="y"):
    l=[rock,paper,scissors]
    y=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
    if y>2:
        print("Wrong input")
    else:
        print(l[y])

        import random
        com=random.randint(0,2)
        print(l[com])
        if(com==0 and y==0):
            print("Draw")
        elif(com==1 and y==1):
            print("Draw")
        elif(com==2 and y==2):
            print("Draw")
        elif(com==0 and y==1):
            print("You win")
        elif(com==0 and y==2):
            print("You lose")
        elif(com==1 and y==0):
            print("You lose")
        elif(com==1 and y==2):
            print("You win")
        elif(com==2 and y==0):
            print("You win")
        elif(com==2 and y==1):
            print("You lose")
        else:
            print("Wrong input")
    y=input("press y to play again\n")