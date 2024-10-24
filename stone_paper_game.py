import random

print("winning rule of the game ROCK PAPER SCISSORS are:")
print("rock vs paper -> paper wins")
print("rock vs scissors -> rock wins")
print("paper vs scissors -> scissors wins")

while True:
    print("1.rock\n2.paper\n3.scissors")
    choice = int(input("enter your choice:"))
    #while choice>3 or choice<1:

    if choice == 1:
        name = 'rock'
    elif choice == 2:
        name = 'paper'
    else:
        name =  'scissors'
    print("user choice is :",name)
    print("now its compter turn...")
    comp_choice =  random.randint(1,3)
    if comp_choice == 1:
        comp_choice_name = 'rock'
    elif comp_choice == 2:
        comp_choice_name = 'paper'
    else:
        comp_choice_name =  'scissors'
    print("computer choice is ...",comp_choice_name)
    print(name ,'VS',comp_choice_name)
    # determine the winner
    if choice==comp_choice:
        result  = "Draw"
    elif (choice==1 and comp_choice==2) or (comp_choice==1 and choice==2):
        result = 'paper'
    elif (choice==1 and comp_choice==3) or (comp_choice==1 and choice==3):
        result = 'rock'
    elif (choice == 2 and comp_choice == 3) or (comp_choice == 2 and choice == 3):
        result = 'Scissors'

    #printing the result
    if result=="Draw":
        print("<==tie==>")
    elif result==name:
        print("<==user win==>")
    else:
        print("<==computer wins==>")
    print("do you want to play again?(y/n)")
    ans =  input()
    if ans=='n':
        break
print("thanks")

        

