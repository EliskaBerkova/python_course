def getMark(points, bonus=0):
    if points + bonus <= 60:
        mark = 5
    elif points + bonus <= 70:
        mark = 4
    elif points + bonus <= 80:
        mark = 3
    elif points + bonus <= 90:
        mark = 2
    else:
        mark = 1
    return mark

points = int(input("zadej pocet bodu v testu: "))
bonus = int(input("zadej pocet bonusovych bodu: "))
mark = getMark(points, bonus)

if mark == 5:
    points = int(input("zadej pocet bodu v opravnem testu: "))
    mark = getMark(points)
print(mark)