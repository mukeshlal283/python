def game(number):
    return number

score = int(game(input("enter the number = ")))

with open("highscore.txt") as f:
    high = int(f.read())

if high < score:
    with open("highscore.txt", "w") as f:
        f.write(str(score))



