import random
def main():
    print ("Im thinking of a number between 1 and 100. Can you guess it?")
    magic_number = random.randrange(1, 101)
    guess = -1
    attempts = 0
    while guess!=magic_number:
        guess = eval(input("Whats the magic number? "))
        if guess > magic_number:
            print ("your to high")
        elif guess < magic_number:
            print ("your to low!")
        else:
            print ("You got it! It took you",attempts,"tries")
        attempts = attempts +1
main()

