names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")


#varianta 1
import random
#number = len(names) - 1
#random = random.randint(0,number)
#name = names[random]
#print(f"{name} is going to buy the meal today!")

#varianta 2
random = random.randint(0,len(names) - 1)
who_will_pay = names[random]
print(f"{who_will_pay} is going to buy the meal today!")