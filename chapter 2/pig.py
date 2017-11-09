#Pig program by: Zach Tokarz, Luke Gentile, and Ryan Larvey.

import random
player1_name = ""
player2_name = ""
player1_score = 0
player2_score = 0
def main():
    global player1_score,player2_score,player1_name,player2_name

    display_welcome()
    ask_player_names()
    roll_dice()

    next_players_turn = 1
    while player1_score <100 and player2_score <100:
        show_scoreboard()
        if next_players_turn == 1:
            print("Its ",player1_name,"'s turn")
            points = play_turn()
            player1_score = player1_score + points
            next_players_turn = 2

        else:
            points = play_turn()
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
    global player1_name, player2_name

    player1_name = input("what is the name of player 1?")
    player2_name = input("what is the name of player 2?")

def roll_dice():
    input("Press enter to roll the dice")

    die = random.randrange(1,6)

    print()
    print(" +---+ ")
    print(" |", die,"|")
    print(" +---+ ")
    print()

    return die


def show_scoreboard():
    global player1_name, player2_name, player1_score, player2_score

    print (player1_name, ": ", player1_score)
    print (player2_name, ": ", player2_score)

def play_turn():
    points = 0
    rolling = True
    while rolling:
        roll= roll_dice()
        if roll == 1:
            rolling = False
            points = 0
            print ("Busted!")
        else:
            rolling = (input("Enter Y to roll agian ") == 'Y')
            points = points + roll

    return points
main()
