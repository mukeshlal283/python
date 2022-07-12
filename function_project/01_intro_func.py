def percent(marks):
    p = (sum(marks)/300)*100
    return p

mark1 = [55, 67, 98]
per1 = percent(mark1)

mark2 = [21, 33, 67]
per2 = percent(mark2)

print(percent(mark1))