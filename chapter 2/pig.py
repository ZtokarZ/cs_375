import random

def main():
    display_welcome()
    ask_player_names()

    next_players_turns = 1
    while player_1 >100 and player_2 >100:
        show_scoreboard()
        if next_players_turn == 1:
            points = play_turn()
            player1_score = player1_score + points
            next_players_turn = 2

        else:
            points = player_turn()
            player2_score = player2_score + points
            next_players_turn = 1


def display_welcome():
    print("""
__________.___  ________
\\______   \\/   |/  _____/
 |     ___/   /   \\  ___
 |    |   |   \\    \\_\\  \\
 |____|   |___|\\______  /
                      \\/
                      """)
    print("Welcome to Pig, first to 100 points wins!")
def ask_player_names():
    eval(input("What is the name of player 1?"))
    eval(input("What is the name of player 2?"))

def show_scoreboard():
    print (player1_score"has" score" points!")
    print (player2_score"has" score" points!")

def player_turn():
    print("")

def player1_score():
    if player1_score is == 100:
        print ("PLayer 1 has won!")
    elif player1_score is > 100:
        eval(input(roll_dice))
def player2_score():
    if player2_score is == 100
        print("Player 2 has won!")
    elif player2_score is > 100

def roll_dice():
    input("Press enter to roll the dice")
    die1 = random.randrange(1,6)
    total = die1

    print()
    print(" +---+  +---+")
    print(" |, die1 , "|")
    print(" +---+  +---+")
    print()
    if roll_dice == 3():
        print ("Busted!")
    main()
