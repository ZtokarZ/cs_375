# SCORES + SCORES / HOW MANY SCORE = AVERAGE
def main():
    total = 0
    scores = 0
    score = input("what's your score?")
    while score !="":
        total=total+eval(score)
        score = input("What's the next score?")
        scores = scores + 1
    print(total / scores)

main()
# This progam will take the average of scores
