# in this it replace ba work to ###

'''with open("sens.txt", "r") as f:
    cat = f.read()

if "donkey" in cat:
    with open("sens.txt", "w") as t:
        t.write(cat.replace("donkey", "##@!$$%#"))'''


#second method 2

with open("sens.txt") as f:
    cat = f.read()

cat = cat.replace("donkey", "#@!%$$##")

with open("sens.txt", "w") as f:
    f.write(cat)

