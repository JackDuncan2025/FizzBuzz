import random
times=int(input('Best of What? '))
x= int(times/2)
y = times%2
x= x+y

while True:
    User = input("Enter a choice (rock, paper, scissors): ").lower()
    picks = ["rock", "paper", "scissors"]
    computer = random.choice(picks)
    print(User, ' Vs. ', computer)

    if User == computer:
        print('tie')
        x += 1
    elif User == "rock":
        if computer == "scissors":
            print('you win')
        else:
            print("you lose")
    elif User == "paper":
        if computer == "rock":
            print('you win')
        else:
            print("you lose")
    elif User == "scissors":
        if computer == "paper":
            print('you win')
        else:
            print("you lose")
    x = x - 1
    if x == 0:
        print('\nEnd')
        break
    
