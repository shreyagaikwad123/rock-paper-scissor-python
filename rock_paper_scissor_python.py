import random
user_wins = 0
computer_wins = 0
options = ['rock','paper','scissor']
while True :
    user_input = input("enter rock/paper/scissor or q for quitting the game ").lower()
    if user_input == 'q':
        break
    if user_input not in options :
        continue
    random_number = random.randint(0,2)
    computer_pick = options[ random_number]
    print("COMPUTER PICKED " , computer_pick , "." )
    if user_input == 'rock' and  computer_pick == 'scissor':
        print("YOU WON !")
        user_wins+=1
    elif user_input == 'paper' and  computer_pick == 'rock':
        print("YOU WON !")
        user_wins+=1
    elif user_input == 'scissor' and  computer_pick == 'paper':
        print("YOU WON !")
        user_wins+=1
    else:
        print("YOU LOST !!")
        computer_wins+=1
print("YOU WON ", user_wins , 'TIMES .')
print("COMPUTER WON ",computer_wins , 'TIMES .')
print("GOODBYE !!!")
