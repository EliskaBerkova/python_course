#def greet_user(name):
    #print(f"Ahoj {name}!")
#greet_user("Elisko")

#def sumTwoNumbers(a, b):
    #return a + b
#result = sumTwoNumbers(10, 15)
#print(result)

def getMark(points):
    if points <= 60:
        mark = 5
    elif points <= 70:
        mark = 4
    elif points <= 80:
        mark = 3
    elif points <= 90:
        mark = 2
    else:
        mark = 1
    return mark

points = int(input("zadej pocet bodu v testu: "))
mark = getMark(points)

if mark == 5:
    points = int(input("zadej pocet bodu v opravnem testu: "))
    mark = getMark(points)
print(mark)


